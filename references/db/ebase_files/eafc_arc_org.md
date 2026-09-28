# 归档组织-eafc_arc_org

## 归档组织-多语言表 tk_eafc_orga_l

- **表名称：** 归档组织-多语言表
- **表名：** tk_eafc_orga_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__tk_eafc_orga_l_0 |  | fid,flocaleid |
| 2 | pk__tk_eafc_orga_l |  | fpkid |

---

## 归档组织-主表 tk_eafc_orga

- **表名称：** 归档组织-主表
- **表名：** tk_eafc_orga

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 实体业务单元 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fk_eafc_change_parent | 变更上级归档组织id | int8 | 64 |  | √ | 0 | 变更上级归档组织id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_arcnumber | 机构号 | varchar | 50 |  | √ | ' ' | 机构号 |
| 8 | fk_eafc_type | 是否全宗 | varchar | 50 |  | √ | ' ' | 是否全宗,枚举: 1 :否 2 :是 |
| 9 | fk_eafc_is_root | 是否为根组织 | bpchar | 1 |  | √ | '0' | 是否为根组织 |
| 10 | fk_eafc_data_source | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :业务单元 2 :手工新增 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_eafc_org_status | 组织状态(弃用) | varchar | 50 |  | √ | ' ' | 组织状态(弃用),枚举: 1 :启用 2 :禁用 |
| 13 | fk_eafc_general_num | 全宗号 | varchar | 50 |  | √ | ' ' | 全宗号 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fk_eafc_general_org | 所属全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 组织状态 | varchar | 50 |  | √ | ' ' | 组织状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fk_fpy_parent_arcorg | 上级归档组织(存储) | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fk_eafc_remark | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 22 | fk_eafc_arc_data | 归档数据 | varchar | 50 |  | √ | ' ' | 归档数据,枚举: 1 :有数据 2 :无数据 |
| 23 | fk_eafc_company_tax | 企业税号 | varchar | 200 |  | √ | ' ' | 企业税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_orga |  | fid |
