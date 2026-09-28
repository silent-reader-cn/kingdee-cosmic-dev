# 审查项-clm_mscon_examineitems

## 检索规则单据体-子表 t_mscon_searchruleentry

- **表名称：** 检索规则单据体-子表
- **表名：** t_mscon_searchruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsearchrule | 检索规则 | varchar | 255 |  | √ | ' ' | 检索规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_searchruleentry_fk |  | fid |
| 2 | pk_mscon_searchruleentry |  | fentryid |

---

## 审查项-多语言表 t_mscon_examineitems_l

- **表名称：** 审查项-多语言表
- **表名：** t_mscon_examineitems_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
| 3 | fexaminerule | 审查规则 | varchar | 770 |  | √ | ' ' | 审查规则 |
| 4 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fkeyword | 检索关键字 | varchar | 399 |  | √ | ' ' | 检索关键字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_examineitems_l_0 |  | fid,flocaleid |
| 2 | pk_mscon_examineitems_l |  | fpkid |

---

## 检索规则单据体-多语言表 t_mscon_searchruleentry_l

- **表名称：** 检索规则单据体-多语言表
- **表名：** t_mscon_searchruleentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fsearchrule | 检索规则 | varchar | 399 |  | √ | ' ' | 检索规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_searchruleentry_l_0 |  | fentryid,flocaleid |
| 2 | pk_mscon_searchruleentry_l |  | fpkid |

---

## 审查项-主表 t_mscon_examineitems

- **表名称：** 审查项-主表
- **表名：** t_mscon_examineitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [审查项分组 mscon_examineitemsgroup](../clmrv_files/mscon_examineitemsgroup.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ftool | 审查工具 | varchar | 50 |  | √ | ' ' | 审查工具,枚举: A :大模型 B :自定义 |
| 10 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 11 | fkeyword | 检索关键字 | varchar | 255 |  | √ | ' ' | 检索关键字 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fexaminerule | 审查规则 | varchar | 512 |  | √ | ' ' | 审查规则 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscon_examineitems |  | fid |
| 2 | idx_mscon_examineitems_m0 |  | fmasterid |
