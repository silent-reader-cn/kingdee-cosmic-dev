# 初始化文件选择器-plm_plmdc_fileselector

## 初始化文件选择器-主表 t_plmdc_fileselector

- **表名称：** 初始化文件选择器-主表
- **表名：** t_plmdc_fileselector

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocalpath | 位置 | varchar | 500 |  | √ | ' ' | 位置 |
| 3 | flocalname | 物理文件名 | varchar | 255 |  | √ | ' ' | 物理文件名 |
| 4 | ftaskid | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |
| 5 | flocalsize | 大小 | varchar | 50 |  | √ | ' ' | 大小 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_fileselector_taskid |  | ftaskid |
| 2 | pk_t_plmdc_fileselector |  | fid |
