# 结算中心设置-ifm_settcentersetting

## 结算中心设置-主表 t_ifm_settlecenterinit

- **表名称：** 结算中心设置-主表
- **表名：** t_ifm_settlecenterinit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fscid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 4 | fusedate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | facceptbusinesssetting | 受理业务设置 | bpchar | 1 |  | √ | '0' | 受理业务设置 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fusestatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 9 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fapplyfundorg | 适用资金组织 | bpchar | 1 |  | √ | '0' | 适用资金组织 |
| 13 | facceptdate | 当前日结日期 | timestamp | 0 |  |  | null | 当前日结日期 |
| 14 | finneraccinit | 是否结束初始化 | bpchar | 1 |  | √ | '0' | 是否结束初始化 |
| 15 | fsettcentersetting | 结算中心设置 | bpchar | 1 |  | √ | '0' | 结算中心设置 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_settlecenterinit |  | fid |
| 2 | idx_ifm_scinit_fscorgid |  | fscorgid |
