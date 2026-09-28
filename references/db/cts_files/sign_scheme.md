# 签名方案-sign_scheme

## 签名组织-子表 t_bd_signschemeorg

- **表名称：** 签名组织-子表
- **表名：** t_bd_signschemeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 签名方案 | int8 | 64 |  | √ | 0 | [签名方案 sign_scheme](../cts_files/sign_scheme.md) |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | varchar | 20 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_signschemeorg_id |  | fid |
| 2 | t_bd_signschemeorg_pkey |  | fentryid |

---

## 签名条件-子表 t_bd_signschemefilter

- **表名称：** 签名条件-子表
- **表名：** t_bd_signschemefilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltername | 过滤条件 | varchar | 100 |  | √ | ' ' | 过滤条件 |
| 3 | ffiltertype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :匹配 |
| 4 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffiltercondition | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_signschemefilter_pkey |  | fentryid |
| 2 | idx_bd_signschemefilter_id |  | fid |

---

## 签名方案-主表 t_bd_signscheme

- **表名称：** 签名方案-主表
- **表名：** t_bd_signscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsignoperate | 签名操作 | varchar | 500 |  | √ | ' ' | 签名操作 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsignfield | 签名字段 | varchar | 2000 |  | √ | ' ' | 签名字段 |
| 5 | fformnumber | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 |
| 6 | fverifyoperate | 验签操作 | varchar | 100 |  | √ | ' ' | 验签操作 |
| 7 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 所属应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_signscheme |  | fid |
| 2 | idx_bd_signscheme_formnumber |  | fformnumber |
