# 渠道用户(已废弃)-ocdbd_channeluser

## 渠道用户(已废弃)-主表 t_ocdbd_channeluser

- **表名称：** 渠道用户(已废弃)-主表
- **表名：** t_ocdbd_channeluser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fiscashier | 收银员 | bpchar | 1 |  | √ | '0' | 收银员 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fisfconsultant | 专属顾问 | bpchar | 1 |  | √ | '0' | 专属顾问 |
| 7 | fsysuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fisdispatcher | 配货员 | bpchar | 1 |  | √ | '0' | 配货员 |
| 9 | fownerid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | fusername | 渠道用户名称 | varchar | 80 |  | √ | ' ' | 渠道用户名称 |
| 11 | fisdptadmin | 销售经理 | bpchar | 1 |  | √ | '0' | 销售经理 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 15 | fusernumber | 渠道用户编码 | varchar | 80 |  | √ | ' ' | 渠道用户编码 |
| 16 | fisbuyer | 采购员 | bpchar | 1 |  | √ | '0' | 采购员 |
| 17 | fiscusorderprocessor | 订单处理员 | bpchar | 1 |  | √ | '0' | 订单处理员 |
| 18 | fissaler | 销售员 | bpchar | 1 |  | √ | '0' | 销售员 |
| 19 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 20 | fcashierid | 收银角色 | int8 | 64 |  | √ | 0 | [收银角色 ocdbd_cashierrole](../ocdbd_files/ocdbd_cashierrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channeluser |  | fid |
| 2 | idx_ocdbd_user_fowfsys |  | fownerid,fsysuserid |
