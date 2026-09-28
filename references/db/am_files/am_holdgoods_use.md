# 实物业务处理-am_holdgoods_use

## 关联信息列表-子表 t_am_goodsuse_sub

- **表名称：** 关联信息列表-子表
- **表名：** t_am_goodsuse_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassociatedtype | 关联单据类型 | varchar | 36 |  | √ | ' ' | 关联单据类型,枚举: A :银行账户管理 B :金融机构 C :票据备查簿 D :定期存款 E :通知存款 F :理财申购 G :银行借款合同 H :企业借款合同 I :担保合同 J :收函登记 K :收证登记 |
| 2 | fbillid | 关联单据ID | varchar | 50 |  | √ | '0' | 关联单据ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillinfo | 关联单据编号 | varchar | 36 |  | √ | ' ' | 关联单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_goodsuse_sub |  | fdetailid |
| 2 | idx_am_goodsuse_sub_fk |  | fentryid |

---

## 变更信息-子表 t_am_goodsuse_change

- **表名称：** 变更信息-子表
- **表名：** t_am_goodsuse_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcdescription | 变更后说明 | varchar | 255 |  | √ | ' ' | 变更后说明 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpropertytype | 变更属性 | varchar | 50 |  | √ | ' ' | 变更属性,枚举: goodsname :实物名称 startdate :生效日期 enddate :失效日期 permission :权限 keeper :保管人 description :说明 associatedtype :关联单据类型 |
| 5 | fcbillid | 关联单据ID | varchar | 50 |  | √ | '0' | 关联单据ID |
| 6 | fckeeperid | 保管人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fafterchange | 变更后 | varchar | 2000 |  | √ | ' ' | 变更后 |
| 8 | fcstartdate | 变更后生效日期 | timestamp | 0 |  |  | null | 变更后生效日期 |
| 9 | fcpermission | 变更后权限 | varchar | 50 |  | √ | ' ' | 变更后权限,枚举: A :查询 B :制单 C :复核 D :管理员 |
| 10 | fcgoodsname | 变更后实物名称 | varchar | 30 |  | √ | ' ' | 变更后实物名称 |
| 11 | fcbillinfo | 关联单据编号 | varchar | 2000 |  | √ | ' ' | 关联单据编号 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcenddate | 变更后失效日期 | timestamp | 0 |  |  | null | 变更后失效日期 |
| 14 | fcassociatedtype | 变更后关联单据类型 | varchar | 50 |  | √ | ' ' | 变更后关联单据类型,枚举: A :银行账户管理 B :金融机构 C :票据备查簿 D :定期存款 E :获取存款 F :理财申购 G :银行借款合同 H :企业借款合同 I :担保合同 J :收函登记 K :收证登记 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_goodsuse_change |  | fentryid |
| 2 | idx_am_goodsuse_change |  | fid |

---

## 实物业务处理-主表 t_am_holdgoods_use

- **表名称：** 实物业务处理-主表
- **表名：** t_am_holdgoods_use

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fstakeholderld | fstakeholderld | varchar | 36 |  | √ | ' ' |  |
| 6 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fstakeholderid | 业务干系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbusinesstype | 业务分类 | varchar | 50 |  | √ | ' ' | 业务分类,枚举: transfer :交接 return :归还 adoption :领用 change :变更 logout :注销 loss :挂失 invalid :作废 |
| 9 | freason | freason | varchar | 512 |  | √ | ' ' |  |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fpredictdate | 预计归还日期 | timestamp | 0 |  |  | null | 预计归还日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 单据编码 | varchar | 36 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_holdgoods_use |  | fid |
| 2 | idx_am_holdgoods_use_num |  | fnumber |

---

## 关联信息列表-子表 t_am_goodsuse_e

- **表名称：** 关联信息列表-子表
- **表名：** t_am_goodsuse_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finventorygoodid | 实物编码 | int8 | 64 |  | √ | 0 | [库存实物管理 am_inventorygoodmanager](../am_files/am_inventorygoodmanager.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fadopterid | 领用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_goodsuse_e |  | fentryid |
| 2 | idx_am_goodsuse_e_fid |  | fid |

---

## 实物业务处理-多语言表 t_am_holdgoods_use_l

- **表名称：** 实物业务处理-多语言表
- **表名：** t_am_holdgoods_use_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | freason | 事由 | varchar | 512 |  | √ | ' ' | 事由 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_holdgoods_use_l |  | fpkid |
| 2 | idx_am_holdgoods_use_l_0 |  | fid,flocaleid |
