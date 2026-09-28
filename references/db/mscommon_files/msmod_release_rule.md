# 预留释放规则-msmod_release_rule

## 对象预留释放顺序-子表 t_msmod_objrelease_entry

- **表名称：** 对象预留释放顺序-子表
- **表名：** t_msmod_objrelease_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freleasebillfield_no | freleasebillfield_no | varchar | 50 |  | √ | ' ' |  |
| 3 | freleasetype | 预留对象类型 | varchar | 50 |  | √ | ' ' | 预留对象类型,枚举: bd_customer :客户 bd_operator :业务员 bos_adminorg :部门 |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 5 | freleasebillfield | freleasebillfield | varchar | 50 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_objrelease_entry |  | fentryid |
| 2 | idx_msmod_objrelease_entry_fid |  | fid |

---

## 基本匹配-子表 t_msmod_releaserule_entry

- **表名称：** 基本匹配-子表
- **表名：** t_msmod_releaserule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freleasecolno | 释放单据字段标识 | varchar | 128 |  | √ | ' ' | 释放单据字段标识 |
| 3 | fstdinvcol | 预留字段 | varchar | 128 |  | √ | ' ' | 预留字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcomparetype | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: = :等于 > :大于 >= :大于等于 < :小于 <= :小于等于 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | freleasecol | 释放单据字段 | varchar | 128 |  | √ | ' ' | 释放单据字段 |
| 8 | fstdinvcolno | 预留字段标识 | varchar | 128 |  | √ | ' ' | 预留字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_releaserule_entry |  | fentryid |
| 2 | idx_msmod_releaserule_entry_id |  | fid |

---

## 预留释放规则-多语言表 t_msmod_release_rule_l

- **表名称：** 预留释放规则-多语言表
- **表名：** t_msmod_release_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_releaserule_l_flid |  | fid,flocaleid |
| 2 | pk_t_msmod_release_rule_l |  | fpkid |

---

## 排序字段-子表 t_msmod_releasesort_entry

- **表名称：** 排序字段-子表
- **表名：** t_msmod_releasesort_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortway | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :升序 desc :降序 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsortfield | 排序字段 | varchar | 128 |  | √ | ' ' | 排序字段 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsortfieldno | 排序字段标识 | varchar | 128 |  | √ | ' ' | 排序字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_releasesort_entry |  | fentryid |
| 2 | idx_msmod_releasesort_entry_id |  | fid |

---

## 对象预留匹配-子表 t_msmod_objrelmat_entry

- **表名称：** 对象预留匹配-子表
- **表名：** t_msmod_objrelmat_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freleasebillfield_no | 预留对象字段标识 | varchar | 50 |  | √ | ' ' | 预留对象字段标识 |
| 3 | fobjreleasetype | 预留对象类型 | varchar | 50 |  | √ | ' ' | 预留对象类型,枚举: bd_customer :客户 bd_operator :业务员 bos_adminorg :部门 |
| 4 | freleasebillfield | 预留对象字段 | varchar | 50 |  | √ | ' ' | 预留对象字段 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_objrelmat_entry |  | fentryid |
| 2 | idx_msmod_objrelmat_entry_fid |  | fid |

---

## 预留释放规则-主表 t_msmod_release_rule

- **表名称：** 预留释放规则-主表
- **表名：** t_msmod_release_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | freservetyperelord | 预留类型释放顺序 | varchar | 50 |  | √ | ' ' | 预留类型释放顺序,枚举: 1 :单据预留优先释放 2 :对象预留优先释放 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | ffiltervalue | 过滤器值 | varchar | 255 |  | √ | ' ' | 过滤器值 |
| 7 | freleasebill | 释放单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ffiltervalue_tag | 过滤器值_详情 | text | 0 |  |  | null | 过滤器值_详情 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_release_rule_freleasebill |  | freleasebill |
| 2 | pk_t_msmod_release_rule |  | fid |
