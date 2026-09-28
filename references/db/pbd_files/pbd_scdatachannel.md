# 集成渠道-pbd_scdatachannel

## 集成渠道-主表 t_pur_scdatachannel

- **表名称：** 集成渠道-主表
- **表名：** t_pur_scdatachannel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisclinkid | 集成云数据连接（多系统对接废弃） | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fchannelclass | 渠道处理类（多系统对接废弃） | varchar | 255 |  | √ | ' ' | 渠道处理类（多系统对接废弃） |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fiscdatasourceid | 集成云数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fchannelfactoryclass | 集成渠道工厂类 | varchar | 255 |  | √ | ' ' | 集成渠道工厂类 |
| 11 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fconnecterp | 连接ERP系统（多系统对接废弃） | varchar | 50 |  | √ | ' ' | 连接ERP系统（多系统对接废弃）,枚举: |
| 15 | fjointchanneltypeid | 集成渠道类型 | varchar | 36 |  | √ | ' ' | 集成渠道类型 pbd_datachanneltype |
| 16 | fisdefault | 是否默认渠道 | bpchar | 1 |  | √ | '0' | 是否默认渠道 |
| 17 | fjointisctype | 集成云连接类型 | varchar | 36 |  | √ | ' ' | 集成云连接类型,枚举: eas :eas（集成EAS系统） k3cloud :k3cloud（集成星空系统） self :self（集成当前苍穹） ierp :ierp（集成远端苍穹） dummy :dummy（非系统集成） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scdatachannel_fnumber |  | fnumber |
| 2 | pk_pur_scdatachannel |  | fid |
| 3 | idx_pur_sdc_fiscdatasourceid |  | fiscdatasourceid |
