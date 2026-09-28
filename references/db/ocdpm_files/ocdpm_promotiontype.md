# 渠道促销类型-ocdpm_promotiontype

## 促销策略-多选基础资料表 t_ocdpm_prostrategy

- **表名称：** 促销策略-多选基础资料表
- **表名：** t_ocdpm_prostrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 渠道促销策略 ocdpm_promotionstrategy |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_prostrategy |  | fpkid |
| 2 | idx_ocdpm_prostrategy_fbid |  | fid,fbasedataid |

---

## 渠道促销类型-主表 t_ocdpm_promotiontype

- **表名称：** 渠道促销类型-主表
- **表名：** t_ocdpm_promotiontype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 促销类型名称 | varchar | 210 |  | √ | ' ' | 促销类型名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisdeploy | 是否配置 | bpchar | 1 |  | √ | '0' | 是否配置 |
| 6 | fpromobjectid | 促销类别 | int8 | 64 |  | √ | 0 | 渠道促销类别 ocdpm_promotionobject |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpromotionpolicyid | fpromotionpolicyid | int8 | 64 |  | √ | 0 |  |
| 9 | fladdertype | 阶梯类型 | bpchar | 1 |  | √ | 'A' | 阶梯类型,枚举: A :阶梯(最高阶梯计算) C :无 |
| 10 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fispresent | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 12 | fpromlink | 促销环节 | bpchar | 1 |  | √ | 'A' | 促销环节,枚举: A :全渠道（渠道间交易） B :供应链 C :全渠道（渠道向企业交易） |
| 13 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fpromrequire | 促销条件 | bpchar | 1 |  | √ | 'A' | 促销条件,枚举: A :按数量 B :按金额 |
| 23 | fnumber | 促销类型编码 | varchar | 80 |  | √ | ' ' | 促销类型编码 |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdpm_promotiontype_createorg |  | fcreateorgid |
| 2 | pk_ocdpm_promotiontype |  | fid |
| 3 | idx_ocdpm_promotiontype_num |  | fnumber |
| 4 | idx_t_ocdpm_promotiontype_master |  | fmasterid |

---

## 单据体-子表 t_ocdpm_promotypeentry

- **表名称：** 单据体-子表
- **表名：** t_ocdpm_promotypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescribe | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fisedit | 是否编辑 | bpchar | 1 |  | √ | '1' | 是否编辑 |
| 4 | ffieldname | ffieldname | varchar | 80 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frequire | 是否必填 | bpchar | 1 |  | √ | '1' | 是否必填 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffieldkey | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 9 | fishide | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotypeentry |  | fentryid |
| 2 | idx_ocdpm_promotype_fid |  | fid |

---

## 渠道促销类型-多语言表 t_ocdpm_promotiontype_l

- **表名称：** 渠道促销类型-多语言表
- **表名：** t_ocdpm_promotiontype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 促销类型名称 | varchar | 210 |  | √ | ' ' | 促销类型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotiontype_l |  | fpkid |
| 2 | idx_ocdpm_promotypel_flid |  | fid,flocaleid |

---

## 渠道促销类型-使用范围表 t_ocdpm_promotiontype_u

- **表名称：** 渠道促销类型-使用范围表
- **表名：** t_ocdpm_promotiontype_u

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
| 1 | pk_t_ocdpm_promotiontype_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdpm_promotiontype_u_uo |  | fuseorgid |

---

## 单据体-多语言表 t_ocdpm_promotypeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_ocdpm_promotypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdescribe | 说明 | varchar | 406 |  | √ | ' ' | 说明 |
| 2 | ffieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotypeentry_l |  | fpkid |
| 2 | idx_ocdpm_promotypeentl_elid |  | fentryid,flocaleid |
