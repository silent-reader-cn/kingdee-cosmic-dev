# 库存实物管理-am_inventorygoodmanager

## 库存实物管理-主表 t_am_inventorygood

- **表名称：** 库存实物管理-主表
- **表名：** t_am_inventorygood

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgoodstatus | 状态 | varchar | 50 |  | √ | 'A' | 状态,枚举: A :已生效 B :业务处理中 C :已作废 D :已挂失 E :已注销 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmanifestid | 清单ID | int8 | 64 |  | √ | 0 | 清单ID |
| 7 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fkeeper | 保管人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 单据状态 | varchar | 50 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 13 | fpermission | 权限 | varchar | 50 |  | √ | ' ' | 权限,枚举: A :查询 B :制单 C :复核 D :管理员 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fgoodsname | 实物名称 | varchar | 50 |  | √ | ' ' | 实物名称 |
| 17 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fadopterid | 领用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fnumber | 实物编号 | varchar | 100 |  | √ | ' ' | 实物编号 |
| 21 | fobjecttypeid | 实物类型 | int8 | 64 |  | √ | 0 | [实物类型设置 am_objecttype](../am_files/am_objecttype.md) |
| 22 | fadoptionstatus | 是否领用 | bpchar | 1 |  | √ | '0' | 是否领用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_inventorygood |  | fid |
| 2 | idx_am_inventorygood_2 |  | fstatus,fenable,fgoodstatus,fadoptionstatus |
| 3 | idx_am_inventorygood_1 |  | fnumber |

---

## 库存实物管理-多语言表 t_am_inventorygood_l

- **表名称：** 库存实物管理-多语言表
- **表名：** t_am_inventorygood_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_inventorygood_l |  | fpkid |
| 2 | idx_am_inventorygood_l_0 |  | fid,flocaleid |

---

## 附件-附件表 t_am_inventorygood_att

- **表名称：** 附件-附件表
- **表名：** t_am_inventorygood_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_am_inventorygood_att_fid |  | fid |
| 2 | pk_t_am_inventorygood_att |  | fpkid |

---

## 关联信息-子表 t_am_inventorygoode

- **表名称：** 关联信息-子表
- **表名：** t_am_inventorygoode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociatedtype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型,枚举: A :银行账户管理 B :金融机构 C :票据备查簿 D :定期存款 E :通知存款 F :理财申购 G :银行借款合同 H :企业借款合同 I :担保合同 J :收函登记 K :收证登记 |
| 3 | fbillid | 关联单据ID | varchar | 50 |  | √ | '0' | 关联单据ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillinfo | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_inventorygoode |  | fentryid |
| 2 | idx_am_inventorygoode_fid |  | fid |
