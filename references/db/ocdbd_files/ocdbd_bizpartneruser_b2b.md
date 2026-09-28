# 我的渠道人员-ocdbd_bizpartneruser_b2b

## 我的渠道人员-多语言表 t_ocdbd_bizpartneruser_l

- **表名称：** 我的渠道人员-多语言表
- **表名：** t_ocdbd_bizpartneruser_l

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
| 1 | idx_ocdbd_bpuserl_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_bizpartneruser_l |  | fpkid |

---

## 我的渠道人员-主表 t_ocdbd_bizpartneruser

- **表名称：** 我的渠道人员-主表
- **表名：** t_ocdbd_bizpartneruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizpartneruserid | 商务伙伴用户 | int8 | 64 |  | √ | 0 | 商务伙伴用户 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fissupportdistritechannel | 自动把配送渠道纳入管理范围 | bpchar | 1 |  | √ | '0' | 自动把配送渠道纳入管理范围 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizpartnertype | 商务伙伴类型 | bpchar | 1 |  | √ | '2' | 商务伙伴类型,枚举: 1 :客户 2 :供应商 |
| 11 | forderchannelid | 所属渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fisadmin | 管理员 | bpchar | 1 |  | √ | '0' | 管理员 |
| 13 | fissupportchildchannel | 自动把下级渠道纳入管理范围 | bpchar | 1 |  | √ | '0' | 自动把下级渠道纳入管理范围 |
| 14 | fusertype | 用户类型 | bpchar | 1 |  | √ | ' ' | 用户类型 |
| 15 | fchannelreqid | 渠道申请 | int8 | 64 |  | √ | 0 | [渠道申请 ocdbd_channelreq](../ocdbd_files/ocdbd_channelreq.md) |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fremark | 用户申请说明 | varchar | 255 |  | √ | ' ' | 用户申请说明 |
| 18 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 22 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 24 | fchanneluserid | fchanneluserid | int8 | 64 |  | √ | 0 |  |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fregistertype | 注册类型 | bpchar | 1 |  | √ | 'A' | 注册类型,枚举: A :正式渠道人员 B :渠道申请人员 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_bpuser_fbizpartid |  | fbizpartnerid |
| 2 | pk_ocdbd_bizpartneruser |  | fid |
| 3 | idx_ocdbd_bpuser_fuserid |  | fuserid |

---

## 全渠道用户角色-多选基础资料表 t_ocdbd_bizpartnerrole

- **表名称：** 全渠道用户角色-多选基础资料表
- **表名：** t_ocdbd_bizpartnerrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [全渠道用户角色 ocdbd_role](../ocdbd_files/ocdbd_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_bizpartnerrole |  | fpkid |
| 2 | idx_ocdbd_bizpartnerrole_fbid |  | fid,fbasedataid |
