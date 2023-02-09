// See https://aka.ms/new-console-template for more information



namespace HelloWorld
{
    class Program
    {
            static void HideIcons()
            {
                RegistryKey myKey = Registry.CurrentUser.OpenSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced", true);
                if (myKey != null)
                {
                    myKey.SetValue("HideIcons", 1);
                    myKey.Close();
                }
            }
        static void Main(string[] args)
        {
            string path = "note1.txt";
            string text = "Hello World\nHello METANIT.COM";
            
            // полная перезапись файла 
            using (StreamWriter writer = new StreamWriter(path, false))
            {
                writer.WriteLineAsync(text);
            }
            // добавление в файл
            using (StreamWriter writer = new StreamWriter(path, true))
            {
                writer.WriteLineAsync("Addition");
                writer.WriteAsync("4,5");
            }
        }
    }
}