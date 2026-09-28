# 限价方案-pmp_pricecontrolscheme

## 【控制强度】分录-子表 t_msbd_pricectlentry

- **表名称：** 【控制强度】分录-子表
- **表名：** t_msbd_pricectlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolintensity | 控制强度 | varchar | 5 |  | √ | ' ' | 控制强度,枚举: warn :预警提示 ban :禁止交易 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_pricectlentry |  | fentryid |
| 2 | idx_msbd_pricectle_fid |  | fid |

---

## 限价方案-多语言表 t_msbd_pricectlscheme_l

- **表名称：** 限价方案-多语言表
- **表名：** t_msbd_pricectlscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_pricectl_l_fid |  | fid,flocaleid |
| 2 | pk_t_msbd_pricectlscheme_l |  | fpkid |

---

## 【字段映射】分录-子表 t_msbd_pricectlmentry

- **表名称：** 【字段映射】分录-子表
- **表名：** t_msbd_pricectlmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcesign | 限价来源字段 | varchar | 50 |  | √ | ' ' | 限价来源字段 |
| 3 | fcontrolsignname | fcontrolsignname | varchar | 80 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcontrolsign | 限价单据字段 | varchar | 50 |  | √ | ' ' | 限价单据字段 |
| 7 | fsourcesignname | fsourcesignname | varchar | 80 |  | √ | ' ' |  |
| 8 | fmatchflag | 映射条件 | varchar | 5 |  | √ | ' ' | 映射条件,枚举: A :等于 B :大于等于 C :大于 D :小于等于 E :小于 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_pricectlmentry |  | fentryid |
| 2 | idx_msbd_pricectlme_fid |  | fid |

---

## 限价方案-主表 t_msbd_pricectlscheme

- **表名称：** 限价方案-主表
- **表名：** t_msbd_pricectlscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 9 | fcontrolentity | 限价单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fuse | 用途 | varchar | 5 |  | √ | ' ' | 用途,枚举: pur :采购 sal :销售 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fcontrolsource | 限价来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_pricectlscheme |  | fid |
| 2 | idx_msbd_pricectl_fnumber |  | fnumber |

---

## 【限价排序】分录-子表 t_msbd_pricectlsentry

- **表名称：** 【限价排序】分录-子表
- **表名：** t_msbd_pricectlsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortsignname | fsortsignname | varchar | 80 |  | √ | ' ' |  |
| 3 | fsortsign | 限价来源字段 | varchar | 50 |  | √ | ' ' | 限价来源字段 |
| 4 | forder | 排序次序 | varchar | 5 |  | √ | ' ' | 排序次序,枚举: A :升序 B :降序 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_pricectlse_fid |  | fid |
| 2 | pk_t_msbd_pricectlsentry |  | fentryid |

---

## 【字段比较】分录-子表 t_msbd_pricectlcentry

- **表名称：** 【字段比较】分录-子表
- **表名：** t_msbd_pricectlcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolcompname | fcontrolcompname | varchar | 80 |  | √ | ' ' |  |
| 3 | fcontrolcomp | 限价单据字段 | varchar | 50 |  | √ | ' ' | 限价单据字段 |
| 4 | fsourcecomp | 限价来源字段 | varchar | 50 |  | √ | ' ' | 限价来源字段 |
| 5 | fcompareflag | 比较条件 | varchar | 5 |  | √ | ' ' | 比较条件,枚举: A :等于 B :大于等于 C :大于 D :小于等于 E :小于 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsourcecompname | fsourcecompname | varchar | 80 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_pricectlcentry |  | fentryid |
| 2 | idx_msbd_pricectlce_fid |  | fid |
