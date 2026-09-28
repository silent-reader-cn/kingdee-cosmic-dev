# 归档组织树形结构-eafc_org_structure

## 归档组织树形结构-主表 tk_eafc_org_structure

- **表名称：** 归档组织树形结构-主表
- **表名：** tk_eafc_org_structure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 3 | fk_eafc_fullnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_fullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 8 | fk_eafc_fullfid | 长id | varchar | 2000 |  | √ | ' ' | 长id |
| 9 | fk_eafc_isleaf | 叶子节点 | bpchar | 1 |  | √ | '1' | 叶子节点 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fk_eafc_arcorg_parent | 上级归档组织id | int8 | 64 |  | √ | 0 | 上级归档组织id |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fk_eafc_org_parent | 上级归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fk_eafc_arcorg | 归档组织id | int8 | 64 |  | √ | 0 | 归档组织id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_org_structure |  | fid |

---

## 归档组织树形结构-多语言表 tk_eafc_org_structure_l

- **表名称：** 归档组织树形结构-多语言表
- **表名：** tk_eafc_org_structure_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fk_eafc_fullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_org_structure_l |  | fpkid |
