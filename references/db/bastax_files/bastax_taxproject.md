# 税务项目信息-bastax_taxproject

## 土地增值税-子表 t_bastax_taxprojectswyt

- **表名称：** 土地增值税-子表
- **表名：** t_bastax_taxprojectswyt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyxqq | 有效期起/降免预征有效期起 | timestamp | 0 |  |  | null | 有效期起/降免预征有效期起 |
| 3 | fyzl | 预征率 | numeric | 23 | 10 | √ | 0 | 预征率 |
| 4 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: 0 :普通住宅 1 :其他类型房地产 2 :非清算业态 3 :非普通住宅 |
| 5 | fyxqz | 有效期止/降免预征有效期止 | timestamp | 0 |  |  | null | 有效期止/降免预征有效期止 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxprojectswyt_fk |  | fid |
| 2 | pk_bastax_taxprojectswyt |  | fentryid |

---

## 税务项目信息-多语言表 t_bastax_taxproject_l

- **表名称：** 税务项目信息-多语言表
- **表名：** t_bastax_taxproject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 税务项目名称 | varchar | 200 |  | √ | ' ' | 税务项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxproject_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_taxproject_l |  | fpkid |

---

## 税务项目信息-主表 t_bastax_taxproject

- **表名称：** 税务项目信息-主表
- **表名：** t_bastax_taxproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 税务项目名称 | varchar | 200 |  | √ | ' ' | 税务项目名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 税务项目类别 | int8 | 64 |  | √ | 0 | 税务项目类别 bastax_taxprojectgroup |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsyslzsl | 适用税率/征收率 | numeric | 23 | 10 | √ | 0 | 适用税率/征收率 |
| 8 | ftaxorgan | 项目主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 9 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbaseproject | 系统项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fsyjhjsff | 是否适用简化计算方法 | bpchar | 1 |  | √ | '0' | 是否适用简化计算方法 |
| 17 | fprojectlocation | 项目所在地 | varchar | 50 |  | √ | ' ' | 项目所在地 |
| 18 | fzsfs | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: 0 :一般计税 1 :简易计税 |
| 19 | fnumber | 税务项目编码 | varchar | 30 |  | √ | ' ' | 税务项目编码 |
| 20 | fdesc | 项目描述 | varchar | 500 |  | √ | ' ' | 项目描述 |
| 21 | fcbfq | 成本分期 | varchar | 50 |  | √ | ' ' | 成本分期,枚举: 1 :一期 2 :二期 3 :三期 4 :四期 5 :五期 6 :六期 7 :七期 8 :八期 9 :九期 10 :十期 |
| 22 | fswqsytfl | 税务清算业态分类 | varchar | 50 |  | √ | ' ' | 税务清算业态分类,枚举: 0 :二分法 1 :三分法 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxproject_forg |  | forg |
| 2 | pk_bastax_taxproject |  | fid |
| 3 | idx_bastax_taxproject_ftaxorg |  | ftaxorg |

---

## 所得税-子表 t_bastax_taxprojectsds

- **表名称：** 所得税-子表
- **表名：** t_bastax_taxprojectsds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsdsyxqz | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsdsyxqq | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 6 | fyjmll | 预计毛利率 | numeric | 23 | 10 | √ | 0 | 预计毛利率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxprojectsds |  | fentryid |
| 2 | idx_bastax_taxprojectsds_fk |  | fid |
