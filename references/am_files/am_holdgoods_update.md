# 实物变动清单-am_holdgoods_update

## 附件-附件表 t_am_postgoodsupdate_att

- **表名称：** 附件-附件表
- **表名：** t_am_postgoodsupdate_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_am_postgoodsatt_fid |  | fid |
| 2 | pk_t_am_postgoodsupdate_att |  | fpkid |

---

## 实物信息列表-子表 t_am_pregoodsupdate

- **表名称：** 实物信息列表-子表
- **表名：** t_am_pregoodsupdate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finventorygoodld | 实名编码 | int8 | 64 |  | √ | 0 | 库存实物管理 am_inventorygoodmanager |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_am_pregoods_fid |  | fid |
| 2 | pk_t_am_pregoodsupdate |  | fentryid |

---

## 附件-附件表 t_am_pregoodsupdate_att

- **表名称：** 附件-附件表
- **表名：** t_am_pregoodsupdate_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_pregoodsupdate_att |  | fpkid |
| 2 | idx_am_pregoodsatt_fid |  | fid |

---

## 实物变动清单-主表 t_am_postgoodsupdates

- **表名称：** 实物变动清单-主表
- **表名：** t_am_postgoodsupdates

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgfield | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpostkeeper | 保管人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fstakeholderid | fstakeholderid | int8 | 64 |  | √ | 0 |  |
| 6 | fbusinesstype | 业务分类 | varchar | 50 |  | √ | ' ' | 业务分类,枚举: change :变更 logout :注销 loss :挂失 invalid :作废 |
| 7 | fprekeeper | 保管人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fpredictdate | 预计归还日期 | timestamp | 0 |  |  | null | 预计归还日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fpoststartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fpregoodsno | 实物编号 | varchar | 50 |  | √ | ' ' | 实物编号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fpreauthority | 权限 | varchar | 50 |  | √ | ' ' | 权限,枚举: A :查询 B :制单 C :复核 D :管理员 |
| 16 | fpostdescribe | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 17 | fprecompany | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fpostgoodsno | 实物编号 | varchar | 50 |  | √ | ' ' | 实物编号 |
| 19 | fstakenholderid | fstakenholderid | varchar | 36 |  | √ | ' ' |  |
| 20 | fpregoodstype | 实物类型 | int8 | 64 |  | √ | 0 | 实物类型设置 am_objecttype |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | forgfieid | forgfieid | int8 | 64 |  | √ | 0 |  |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fstakeholderld | 业务干系人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fpreenddate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 27 | fmulcombofield | 权限 | varchar | 50 |  | √ | ' ' | 权限,枚举: A :查询 B :制单 C :复核 D :管理员 |
| 28 | fprestartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 29 | freason | 事由 | varchar | 50 |  | √ | ' ' | 事由 |
| 30 | fpostenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 31 | fpregoodsname | 实物名称 | varchar | 50 |  | √ | ' ' | 实物名称 |
| 32 | fbasedatafield1 | 实物类型 | int8 | 64 |  | √ | 0 | 实物类型设置 am_objecttype |
| 33 | fpredescribe | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 34 | fpregoodstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :已生效 B :业务处理中 C :已作废 D :已挂失 E :已注销 |
| 35 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fbillstatusfield | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :已生效 B :业务处理中 C :已作废 D :已挂失 E :已注销 |
| 37 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 39 | fpostgoodsname | 实物名称 | varchar | 50 |  | √ | ' ' | 实物名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_postgoodsupdates |  | fid |
| 2 | idx_t_am_goodsupdates_billno |  | fnumber |

---

## 变更后关联信息-子表 t_am_postgoodsupdate_sub

- **表名称：** 变更后关联信息-子表
- **表名：** t_am_postgoodsupdate_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fpostassociatedtype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型,枚举: A :银行账户管理 B :金融机构 C :票据备查簿 D :定期存款 E :获取存款 F :理财申购 G :银行借款合同 H :企业借款合同 I :担保合同 J :收函登记 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fpostbillinfo | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_am_goodsupdate_fid |  | fid |
| 2 | pk_t_am_postgoodsupdate_sub |  | fentryid |

---

## 实物变动清单-多语言表 t_am_postgoodsupdates_l

- **表名称：** 实物变动清单-多语言表
- **表名：** t_am_postgoodsupdates_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_postgoodsupdates_l |  | fpkid |
| 2 | idx_am_postgoodsupdates_l |  | fid,flocaleid |

---

## 关联信息列表-子表 t_am_pregoodsupdate_sub

- **表名称：** 关联信息列表-子表
- **表名：** t_am_pregoodsupdate_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassociatedtype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型,枚举: A :银行账户管理 B :金融机构 C :票据备查簿 D :定期存款 E :获取存款 F :理财申购 G :银行借款合同 H :企业借款合同 I :担保合同 J :收函登记 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillinfo | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_pregoodsupdate_sub |  | fdetailid |
| 2 | idx_am_pregoodsupdate_fid |  | fentryid |
