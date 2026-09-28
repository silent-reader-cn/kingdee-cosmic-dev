# 税务组织映射关系-tctb_orgmaprelation

## 税务组织映射关系-多语言表 t_tctb_orgmap_taxorg_l

- **表名称：** 税务组织映射关系-多语言表
- **表名：** t_tctb_orgmap_taxorg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmap_taxorg_l |  | fpkid |
| 2 | idx_tctb_orgmap_taxorg_l_0 |  | fentryid,flocaleid |

---

## 映射关系-子表 t_tctb_orgmap_busobject

- **表名称：** 映射关系-子表
- **表名：** t_tctb_orgmap_busobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxcategory | 适用税种编码 | varchar | 400 |  | √ | ' ' | 适用税种编码 |
| 2 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fbusinessid | 业务对象id | varchar | 80 |  | √ | ' ' | 业务对象id |
| 4 | fbusinessnumber | 业务对象编码 | varchar | 80 |  | √ | ' ' | 业务对象编码 |
| 5 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 6 | fbusinessname | 业务对象名称 | varchar | 150 |  | √ | ' ' | 业务对象名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 11 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmap_busobject |  | fdetailid |
| 2 | idx_tctb_orgmap_busobject_fk |  | fentryid |

---

## 税务组织映射关系-主表 t_tctb_orgmap_taxorg

- **表名称：** 税务组织映射关系-主表
- **表名：** t_tctb_orgmap_taxorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 映射方案 | int8 | 64 |  | √ | 0 | 税务组织映射方案 tctb_orgmapentity |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 9 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmap_taxorg |  | fentryid |
| 2 | idx_tctb_orgmap_taxorg_fk |  | fid |
