# 自动结算方案-ism_autosettlescheme

## 下级业务组织-多选基础资料表 t_ism_autosettle_suborg

- **表名称：** 下级业务组织-多选基础资料表
- **表名：** t_ism_autosettle_suborg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_autosettle_suborg_fk |  | fid |
| 2 | pk_ism_autosettle_suborg |  | fpkid |

---

## 自动结算方案-主表 t_ism_autosettlescheme

- **表名称：** 自动结算方案-主表
- **表名：** t_ism_autosettlescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 3 | facctorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fauditarbill | 审核应收结算清单 | bpchar | 1 |  | √ | '0' | 审核应收结算清单 |
| 6 | frollsettle | 滚动结算 | bpchar | 1 |  | √ | '1' | 滚动结算 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsettlezeroprice | 结算价等于0生成结算清单 | bpchar | 1 |  | √ | '0' | 结算价等于0生成结算清单 |
| 13 | fsuborg | fsuborg | int8 | 64 |  | √ | 0 |  |
| 14 | fmonthsettle | 按自然月结算 | bpchar | 1 |  | √ | '1' | 按自然月结算 |
| 15 | fexceplan | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 16 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 17 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fauditapbill | 审核应付结算清单 | bpchar | 1 |  | √ | '0' | 审核应付结算清单 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fcreatearbill | 创建应收结算清单 | bpchar | 1 |  | √ | '1' | 创建应收结算清单 |
| 22 | fmaxentrycount | 生成结算清单行数 | int8 | 64 |  | √ | 0 | 生成结算清单行数 |
| 23 | fexecplanbd | fexecplanbd | varchar | 50 |  | √ | ' ' |  |
| 24 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 28 | fcreateapbill | 创建应付结算清单 | bpchar | 1 |  | √ | '1' | 创建应付结算清单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_autosettlescheme |  | fid |

---

## 结算业务单据范围-子表 t_ism_autosettlescheme_e

- **表名称：** 结算业务单据范围-子表
- **表名：** t_ism_autosettlescheme_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewbillfilter | 过滤条件（后台） | varchar | 255 |  | √ | ' ' | 过滤条件（后台） |
| 3 | fparmentitykey | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnewbillfilter_tag | 过滤条件（后台）_详情 | text | 0 |  |  | null | 过滤条件（后台）_详情 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_autosettlescheme_e_fk |  | fentryid |
| 2 | pk_ism_autosettlescheme_e |  | fentryid |

---

## 自动结算方案-多语言表 t_ism_autosettlescheme_l

- **表名称：** 自动结算方案-多语言表
- **表名：** t_ism_autosettlescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fexceplanlang | 执行计划多语言 | varchar | 255 |  | √ | ' ' | 执行计划多语言 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_autosettlescheme_l |  | fpkid |
| 2 | idx_ism_autosettlescheme_l_0 |  | fid,flocaleid |
