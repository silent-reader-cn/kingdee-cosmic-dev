# 灰度特性管理-lic_grayfeature

## 灰度特性管理-主表 t_lic_grayfeature

- **表名称：** 灰度特性管理-主表
- **表名：** t_lic_grayfeature

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 许可申请状态 | varchar | 30 |  | √ | ' ' | 许可申请状态,枚举: 0 :未申请 1 :申请中 2 :申请成功（待更新灰度许可） 3 :申请失败 10 :申请成功 11 :灰度结束 |
| 3 | fenddate | 租赁结束时间 | timestamp | 0 |  |  | null | 租赁结束时间 |
| 4 | fremindersign | 是否需要提醒 | varchar | 30 |  | √ | ' ' | 是否需要提醒 |
| 5 | fapplicationdate | 灰度许可申请时间 | timestamp | 0 |  |  | null | 灰度许可申请时间 |
| 6 | fbegindate | 租赁起始时间 | timestamp | 0 |  |  | null | 租赁起始时间 |
| 7 | fgrayenddate | 灰度过期时间 | timestamp | 0 |  |  | null | 灰度过期时间 |
| 8 | fschemeid | 灰度特性 | int8 | 64 |  | √ | 0 | 灰度特性 lic_grayfeaturescheme |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_grayfeature |  | fid |
| 2 | idx_lic_grayfeature_scheme |  | fschemeid |
