# 渠道分类信息-ocdbd_channel_classes

## 渠道分类信息-主表 t_ocdbd_channelclasses

- **表名称：** 渠道分类信息-主表
- **表名：** t_ocdbd_channelclasses

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 渠道主键 | int8 | 64 |  | √ | 0 | 渠道主键 |
| 2 | fclassstandardid | 渠道分类标准 | int8 | 64 |  | √ | 0 | [渠道分类标准 ocdbd_channel_standard](../ocdbd_files/ocdbd_channel_standard.md) |
| 3 | fchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channelclasses |  | fentryid |
| 2 | idx_ocdbd_chlclasses_fid |  | fid |
