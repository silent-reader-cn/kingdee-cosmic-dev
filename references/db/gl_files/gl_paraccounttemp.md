# 平行记账模板-gl_paraccounttemp

## 平行记账模板-主表 t_gl_paraccounttemp

- **表名称：** 平行记账模板-主表
- **表名：** t_gl_paraccounttemp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 模板类别 | int8 | 64 |  | √ | 0 | [平行记账模板类别 gl_paraccounttemptype](../gl_files/gl_paraccounttemptype.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmergeoption | 预算分录合并选项 | bpchar | 1 |  | √ | ' ' | 预算分录合并选项,枚举: A :不合并 B :摘要不同，允许合并 C :摘要不同，不允许合并 |
| 14 | fpartialmatch | 允许部分匹配 | bpchar | 1 |  | √ | ' ' | 允许部分匹配 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_paraccounttemp_fnumber |  | fnumber |
| 2 | pk_gl_paraccounttemp |  | fid |
| 3 | idx_gl_paraccounttemp_forgid |  | forgid |

---

## 平行记账模板-多语言表 t_gl_paraccounttemp_l

- **表名称：** 平行记账模板-多语言表
- **表名：** t_gl_paraccounttemp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_paraccounttemp_l |  | fpkid |
| 2 | idx_gl_paraccounttemp_l |  | fid,flocaleid |

---

## 单据体-子表 t_gl_paraccounttempentry

- **表名称：** 单据体-子表
- **表名：** t_gl_paraccounttempentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrydc | 方向 | varchar | 2 |  | √ | '1' | 方向,枚举: 1 :借 -1 :贷 |
| 3 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 4 | fbmaccountid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 5 | fbmentrydc | 方向 | varchar | 2 |  | √ | '1' | 方向,枚举: 1 :借 -1 :贷 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 8 | fbmassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 9 | fdiffprojectid | 差异项目 | int8 | 64 |  | √ | 0 | [差异项目 gl_diffitem](../gl_files/gl_diffitem.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | faccountid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_paraccounttempentry |  | fentryid |
| 2 | idx_gl_paraccttemp_entry_fid |  | fid |
