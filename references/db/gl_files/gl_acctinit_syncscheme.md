# 同步方案-gl_acctinit_syncscheme

## 同步方案-多语言表 t_gl_sysnscheme_l

- **表名称：** 同步方案-多语言表
- **表名：** t_gl_sysnscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmeaunitcontent | 计量单位内容 | text | 0 |  | √ | ' ' | 计量单位内容 |
| 3 | fasstcontent | 核算维度内容 | text | 0 |  | √ | ' ' | 核算维度内容 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | faccountfilter | 科目过滤内容 | text | 0 |  | √ | ' ' | 科目过滤内容 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_sysnscheme_l |  | fpkid |
| 2 | idx_gl_sysnscheme_l |  | fid,flocaleid |

---

## 同步方案-主表 t_gl_sysnscheme

- **表名称：** 同步方案-主表
- **表名：** t_gl_sysnscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdc | 方向 | varchar | 2 |  | √ | ' ' | 方向,枚举: 1 :借 -1 :贷 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fsourceapp | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :应收款管理 2 :应付款管理 |
| 7 | fasstcontent | 核算维度内容 | text | 0 |  | √ | ' ' | 核算维度内容 |
| 8 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmeaunitcontent | 计量单位内容 | text | 0 |  | √ | ' ' | 计量单位内容 |
| 12 | fcheckenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 13 | faccountfilter | 科目过滤内容 | text | 0 |  | √ | ' ' | 科目过滤内容 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | faccountid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_sysnscheme |  | fid |
| 2 | idx_gl_sysnscheme_fbookid |  | fbookid |
