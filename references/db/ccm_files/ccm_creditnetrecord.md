# 信用网控记录-ccm_creditnetrecord

## 信用网控记录-主表 t_ccm_creditnetrecord

- **表名称：** 信用网控记录-主表
- **表名：** t_ccm_creditnetrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveid | 控制档案对象 | int8 | 64 |  | √ | 0 | 控制档案对象 |
| 3 | fupdatebillno | 做信用更新的单据编号 | varchar | 100 |  | √ | ' ' | 做信用更新的单据编号 |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 6 | fctrltype | 控制类型 | varchar | 30 |  | √ | ' ' | 控制类型,枚举: update :信用更新 recal :信用重算 |
| 7 | fentitykey | 操作业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_creditnetrecord |  | farchiveid |
| 2 | pk_ccm_creditnetrecord |  | fid |
