# 内部交易单据字段设置-ism_innerbillfielddata

## 内部交易单据字段设置-主表 t_ism_innerbillfielddata

- **表名称：** 内部交易单据字段设置-主表
- **表名：** t_ism_innerbillfielddata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态 |
| 4 | fbillentry | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |
| 5 | fisvirtualbill | 是否虚单 | varchar | 50 |  | √ | ' ' | 是否虚单 |
| 6 | finowner | 调入货主 | varchar | 50 |  | √ | ' ' | 调入货主 |
| 7 | fentitykey | 内部单据业务实体 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fbillentry_lk | 关联实体标识 | varchar | 50 |  | √ | ' ' | 关联实体标识 |
| 9 | fbilldate | 单据日期 | varchar | 50 |  | √ | ' ' | 单据日期 |
| 10 | foutowner | 调出货主 | varchar | 50 |  | √ | ' ' | 调出货主 |
| 11 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_innerbillfielddata |  | fid |
| 2 | idx_ism_innerbillfielddata |  | fentitykey |
