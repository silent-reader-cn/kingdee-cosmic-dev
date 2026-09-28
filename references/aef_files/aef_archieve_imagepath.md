# 归档影像路径-aef_archieve_imagepath

## 归档影像路径-主表 t_aef_archieve_imagepath

- **表名称：** 归档影像路径-主表
- **表名：** t_aef_archieve_imagepath

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fimagetype | 影像类型 | varchar | 30 |  | √ | ' ' | 影像类型,枚举: 1 :自身PDF 0 :附件影像 |
| 3 | ffilename | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 4 | farchievetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 5 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 6 | fimagepath | 存储路径 | varchar | 200 |  | √ | ' ' | 存储路径 |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | farchieveid | 归档人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aef_archieve_imagepath_pkey |  | fid |
| 2 | idx_aef_archieve_imagepath |  | fbillid,fbilltype |
