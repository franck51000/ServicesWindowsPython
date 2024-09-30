import win32serviceutil
import win32service
import win32event
import subprocess
import os
import time
import sys

class CameraService(win32serviceutil.ServiceFramework):
    _svc_name_ = "CameraService"
    _svc_display_name_ = "Python Camera Management Service"
    _svc_description_ = "Service Windows qui lance un processus Python de gestion de caméra"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_running = True

    def SvcStop(self):
        # Méthode appelée pour arrêter le service
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        # Méthode appelée pour démarrer le service
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        
        # Journaux pour déboguer
        log_file = "C:\\python\\service_log.txt"
        with open(log_file, "a") as log:
            log.write("Le service a démarré à : {}\n".format(time.ctime()))
            log.write("Interpréteur Python utilisé : {}\n".format(sys.executable))
        
        # Chemin vers l'interpréteur Python et le script Python qui doit être exécuté
        python_executable = "C:\\Program Files\\Python39\\python.exe"
        script_path = "C:\\python\\test.py"
        
        try:
            # Commande pour lancer le processus Python
            command = f'"{python_executable}" "{script_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            
            # Surveiller le processus tant que le service est en cours d'exécution
            while self.is_running:
                # Lire les sorties standard et erreurs standard
                stdout, stderr = process.communicate()
                with open(log_file, "a") as log:
                    if stdout:
                        log.write("STDOUT: {}\n".format(stdout.decode()))
                    if stderr:
                        log.write("STDERR: {}\n".format(stderr.decode()))

                # Vérifier si le processus est toujours actif
                if process.poll() is not None:
                    with open(log_file, "a") as log:
                        log.write("Le processus s'est arrêté de manière inattendue à : {}\n".format(time.ctime()))
                    break  # Si le processus s'arrête, quitter la boucle

                # Pause avant de vérifier à nouveau
                win32event.WaitForSingleObject(self.hWaitStop, 5000)
        
        except Exception as e:
            # Gestion des exceptions et écriture dans le journal
            with open(log_file, "a") as log:
                log.write("Erreur pendant l'exécution du service : {}\n".format(str(e)))
        
        # Nettoyage: s'assurer que le processus se termine
        if process.poll() is None:
            process.terminate()

        with open(log_file, "a") as log:
            log.write("Le service s'est arrêté à : {}\n".format(time.ctime()))

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(CameraService)
