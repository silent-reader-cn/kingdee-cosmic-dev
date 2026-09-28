# 指引步骤关联页面&#x2f;表单-xkguide_ref

## 指引步骤关联页面&#x2f;表单-主表 t_xkbase_guide_ref

- **表名称：** 指引步骤关联页面&#x2f;表单-主表
- **表名：** t_xkbase_guide_ref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fguidestepid | 指引步骤 | int8 | 64 |  | √ | 0 | 指引步骤 xkguide_step |
| 3 | flinkparams | 链接参数（json） | text | 0 |  |  | ' ' | 链接参数（json） |
| 4 | findex | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 5 | flinkname | 链接名称 | varchar | 50 |  | √ | ' ' | 链接名称 |
| 6 | flinktype | 链接类型 | varchar | 10 |  | √ | ' ' | 链接类型,枚举: url :url链接 menu :菜单 |
| 7 | flinkstyle | 链接的样式（json） | text | 0 |  |  | ' ' | 链接的样式（json） |
| 8 | fformid | 业务对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fisgrouporg | 是否按组织隔离 | bpchar | 1 |  | √ | '0' | 是否按组织隔离 |
| 10 | fscope | 查询范围 | varchar | 10 |  | √ | '0' | 查询范围,枚举: 0 :单组织/多组织可查 1 :单组织可查 2 :多组织可查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_guide_ref |  | fid |
| 2 | idx_g_ref_stepid |  | fguidestepid |

---

## 指引步骤关联页面&#x2f;表单-多语言表 t_xkbase_guide_ref_l

- **表名称：** 指引步骤关联页面&#x2f;表单-多语言表
- **表名：** t_xkbase_guide_ref_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flinkname | 链接名称 | varchar | 500 |  | √ | ' ' | 链接名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_guide_ref_l |  | fpkid |
| 2 | idx_g_ref_l_fid |  | fid |
