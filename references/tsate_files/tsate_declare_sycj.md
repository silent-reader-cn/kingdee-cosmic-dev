# 税企直连-税源采集-tsate_declare_sycj

## 税企直连-税源采集-主表 t_tsate_declare_sycj

- **表名称：** 税企直连-税源采集-主表
- **表名：** t_tsate_declare_sycj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsbxx | 申报信息 | varchar | 255 |  | √ | ' ' | 申报信息 |
| 6 | fmaindataid | 主数据ID | varchar | 50 |  | √ | ' ' | 主数据ID |
| 7 | fsbxx_tag | 申报信息_详情 | text | 0 |  |  | null | 申报信息_详情 |
| 8 | fsyxx_tag | 税源信息_详情 | text | 0 |  |  | null | 税源信息_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsyxx | 税源信息 | varchar | 255 |  | √ | ' ' | 税源信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sycj_maindataid |  | fmaindataid |
| 2 | pk_tsate_declare_sycj |  | fid |
