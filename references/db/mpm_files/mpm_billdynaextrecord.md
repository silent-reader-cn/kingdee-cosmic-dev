# 单据动态扩展记录-mpm_billdynaextrecord

## 单据动态扩展记录-主表 t_mpm_billdynaextrecord

- **表名称：** 单据动态扩展记录-主表
- **表名：** t_mpm_billdynaextrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextendid | 元数据扩展id | varchar | 50 |  | √ | ' ' | 元数据扩展id |
| 3 | fparentmetaid | 父元数据id | varchar | 50 |  | √ | ' ' | 父元数据id |
| 4 | fparentmetaname | 父元数据名 | varchar | 80 |  | √ | ' ' | 父元数据名 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbillobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fextendname | 元数据扩展名 | varchar | 80 |  | √ | ' ' | 元数据扩展名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_billdynaextrecord |  | fid |
| 2 | idx_mpm_billdynaextrec_bo |  | fbillobjectid |
