# 渠道组织信息-ocdbd_channel_org

## 渠道组织信息-主表 t_ocdbd_channelorginfo

- **表名称：** 渠道组织信息-主表
- **表名：** t_ocdbd_channelorginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 2 | fprovinceid | fprovinceid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 4 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 5 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlorginfo_fid |  | fid |
| 2 | pk_ocdbd_channelorginfo |  | fentryid |
