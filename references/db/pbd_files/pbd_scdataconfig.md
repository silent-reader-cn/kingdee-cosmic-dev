# 协同数据处理参数配置-pbd_scdataconfig

## 协同数据处理参数配置-主表 t_pur_scdataconfig

- **表名称：** 协同数据处理参数配置-主表
- **表名：** t_pur_scdataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 参数配置描述 | varchar | 255 |  | √ | ' ' | 参数配置描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fscdatachannelid | 数据处理渠道 | varchar | 36 |  | √ | ' ' | [集成渠道 pbd_scdatachannel](../pbd_files/pbd_scdatachannel.md) |
| 8 | fstoreclass | 处理插件 | varchar | 255 |  | √ | ' ' | 处理插件 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sdc_fnumber |  | fnumber |
| 2 | pk_t_pur_scdataconfig |  | fid |
