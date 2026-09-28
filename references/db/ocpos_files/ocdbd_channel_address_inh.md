# 店铺收货地址-ocdbd_channel_address_inh

## 店铺收货地址-主表 t_ocdbd_chl_address

- **表名称：** 店铺收货地址-主表
- **表名：** t_ocdbd_chl_address

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbdaddressid | 客户地址 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 5 | fisfromcustomer | 由客户导入 | bpchar | 1 |  | √ | '0' | 由客户导入 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcontactname | 收货人 | varchar | 50 |  | √ | ' ' | 收货人 |
| 8 | femail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 9 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftelephone | 收货人电话 | varchar | 255 |  | √ | ' ' | 收货人电话 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | falladdress | 地址全名 | varchar | 255 |  | √ | ' ' | 地址全名 |
| 14 | fadmindivisionid | 省/市/区 | varchar | 36 |  | √ | ' ' | 省/市/区 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | forderchannelid | 店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 18 | ffixedte | 固定电话 | varchar | 255 |  | √ | ' ' | 固定电话 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | flinkmanid | 客户联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 23 | fisdefault | 设为默认 | bpchar | 1 |  | √ | '0' | 设为默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chladdress_ochl |  | forderchannelid |
| 2 | idx_ocdbd_chladdress_num |  | fnumber |
| 3 | pk_ocdbd_chl_address |  | fid |

---

## 店铺收货地址-多语言表 t_ocdbd_chl_address_l

- **表名称：** 店铺收货地址-多语言表
- **表名：** t_ocdbd_chl_address_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chladdressl_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_chl_address_l |  | fpkid |
