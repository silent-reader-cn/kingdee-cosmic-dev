# 供货关系-ocdbd_supplier

## 供货关系-主表 t_ocdbd_channel_auth

- **表名称：** 供货关系-主表
- **表名：** t_ocdbd_channel_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentinvtype | 显示上级库存 | bpchar | 1 |  | √ | ' ' | 显示上级库存,枚举: 0 :不显示 1 :模糊显示 2 :精确显示 |
| 3 | fdiscountrate | 折扣率（小数） | numeric | 23 | 10 | √ | 0 | 折扣率（小数） |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisagentdistribut | 代配送商 | bpchar | 1 |  | √ | '0' | 代配送商 |
| 8 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fshippingtypecontrol | 运输方式控制 | bpchar | 1 |  | √ | '0' | 运输方式控制 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fleadtime | 订货提前期（天） | int8 | 64 |  | √ | 0 | 订货提前期（天） |
| 17 | fregion | fregion | int8 | 64 |  | √ | 0 |  |
| 18 | fhundredrate | 折扣率（%） | numeric | 23 | 10 | √ | 0 | 折扣率（%） |
| 19 | fis3distribut | 第三方配送 | bpchar | 1 |  | √ | '0' | 第三方配送 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 23 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 28 | flogistics | flogistics | varchar | 30 |  | √ | '0' |  |
| 29 | fenabletime | fenabletime | timestamp | 0 |  |  | null |  |
| 30 | fonlycash | 仅现销 | bpchar | 1 |  | √ | '0' | 仅现销 |
| 31 | fmarketability | 可销商品控制 | bpchar | 1 |  | √ | '0' | 可销商品控制 |
| 32 | fupdowncontrol | 渠道上下架控制 | bpchar | 1 |  | √ | '0' | 渠道上下架控制 |
| 33 | fadminorgid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fchannelclassid | 所属渠道分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 35 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 37 | fisnotintax | 不含税 | bpchar | 1 |  | √ | '0' | 不含税 |
| 38 | falias | 别名 | varchar | 80 |  | √ | ' ' | 别名 |
| 39 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 40 | fisconsignment | 委托代销 | bpchar | 1 |  | √ | '0' | 委托代销 |
| 41 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 42 | fcreditcontrol | 信用控制 | bpchar | 1 |  | √ | '0' | 信用控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlauth_ochl |  | forderchannelid |
| 2 | idx_t_ocdbd_channel_auth_createorg |  | fcreateorgid |
| 3 | pk_ocdbd_channel_auth |  | fid |
| 4 | idx_ocdbd_chlauth_createtime |  | fcreatetime |
| 5 | idx_ocdbd_chlauth_schl |  | fsalechannelid |
| 6 | idx_t_ocdbd_channel_auth_master |  | fmasterid |

---

## 供货关系-使用范围表 t_ocdbd_channel_auth_u

- **表名称：** 供货关系-使用范围表
- **表名：** t_ocdbd_channel_auth_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ocdbd_channel_auth_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdbd_channel_auth_u_uo |  | fuseorgid |

---

## 供货关系-多语言表 t_ocdbd_channel_auth_l

- **表名称：** 供货关系-多语言表
- **表名：** t_ocdbd_channel_auth_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | falias | 别名 | varchar | 80 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channel_auth_l |  | fpkid |
| 2 | idx_ocdbd_chlauthl_flid |  | fid,flocaleid |
