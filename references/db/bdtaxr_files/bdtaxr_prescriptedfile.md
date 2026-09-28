# 预置脚本文件-bdtaxr_prescriptedfile

## 预置脚本文件-主表 t_bdtaxr_prescriptedfile

- **表名称：** 预置脚本文件-主表
- **表名：** t_bdtaxr_prescriptedfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprescriptedid | 预置脚本ID | int8 | 64 |  | √ | 0 | 预置脚本ID |
| 3 | fcontent_tag | 文件内容_详情 | text | 0 |  |  | null | 文件内容_详情 |
| 4 | fprescriptedentryid | 预置脚本分录ID | int8 | 64 |  | √ | 0 | 预置脚本分录ID |
| 5 | fcontent | 文件内容 | varchar | 255 |  | √ | ' ' | 文件内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_prescriptedfile |  | fid |
| 2 | idx_bdtaxr_prefile_fid |  | fprescriptedid,fprescriptedentryid |
