# 核算维度值范围设置-gl_assgrpfilter

## 值范围-多选基础资料表 t_gl_assgrpfiltermulval

- **表名称：** 值范围-多选基础资料表
- **表名：** t_gl_assgrpfiltermulval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [科目影响因素（旧） ai_vchentrytype](../ai_files/ai_vchentrytype.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_assgrpfiltermulval_pkey |  | fpkid |
| 2 | idx_gl_assgrpfiltermulval |  | fentryid |

---

## 核算维度值范围设置-主表 t_gl_assgrpfilter

- **表名称：** 核算维度值范围设置-主表
- **表名：** t_gl_assgrpfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '7' |  |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 15 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_assgrpfilter_createorg |  | fcreateorgid |
| 2 | t_gl_assgrpfilter_pkey |  | fid |
| 3 | idx_t_gl_assgrpfilter_master |  | fmasterid |
| 4 | idx_gl_assgrpfilter |  | forgid,faccounttableid |

---

## 科目核算维度值范围设置-子表 t_gl_assgrpfilterentry

- **表名称：** 科目核算维度值范围设置-子表
- **表名：** t_gl_assgrpfilterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 3 | ffiltercondition_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ffiltervaldesc | 值范围 | varchar | 255 |  | √ | ' ' | 值范围 |
| 6 | ffilterdesc | 过滤条件 | varchar | 200 |  | √ | ' ' | 过滤条件 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffiltercondition | 过滤条件 | varchar | 510 |  | √ | ' ' | 过滤条件 |
| 9 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_assgrpfilterentry_pkey |  | fentryid |
| 2 | idx_gl_assgrpfilterentry |  | fid |

---

## 核算维度值范围设置-多语言表 t_gl_assgrpfilter_l

- **表名称：** 核算维度值范围设置-多语言表
- **表名：** t_gl_assgrpfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_assgrpfilter_l |  | fid,flocaleid |
| 2 | t_gl_assgrpfilter_l_pkey |  | fpkid |
