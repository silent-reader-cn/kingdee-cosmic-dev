# 归档体系_旧-eafc_org

## 归档体系_旧-多语言表 tk_eafc_org_l

- **表名称：** 归档体系_旧-多语言表
- **表名：** tk_eafc_org_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 全宗名称 | varchar | 50 |  | √ | ' ' | 全宗名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__tk_eafc_org_l_0 |  | fid,flocaleid |
| 2 | pk__tk_eafc_org_l |  | fpkid |

---

## 归档体系_旧-主表 tk_eafc_org

- **表名称：** 归档体系_旧-主表
- **表名：** tk_eafc_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 实体业务单元 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 全宗名称 | varchar | 50 |  | √ | ' ' | 全宗名称 |
| 4 | fk_eafc_arcnumber | 全宗号 | varchar | 50 |  | √ | ' ' | 全宗号 |
| 5 | fk_eafc_type | 形态 | varchar | 50 |  | √ | ' ' | 形态,枚举: 1 :组织 2 :全宗 |
| 6 | fk_eafc_data_source | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :业务单元 2 :手工新增 |
| 7 | fk_eafc_org_status | 组织状态 | varchar | 50 |  | √ | ' ' | 组织状态,枚举: 1 :启用 2 :禁用 |
| 8 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fk_eafc_textfield | 上级全宗 | varchar | 50 |  | √ | ' ' | 上级全宗 |
| 10 | fnumber | 全宗编号 | varchar | 50 |  | √ | ' ' | 全宗编号 |
| 11 | fk_eafc_remark | 全宗描述 | varchar | 200 |  | √ | ' ' | 全宗描述 |
| 12 | fk_eafc_arc_data | 归档数据 | varchar | 50 |  | √ | ' ' | 归档数据,枚举: 1 :有数据 2 :无数据 |
| 13 | fk_eafc_company_tax | 企业税号 | varchar | 200 |  | √ | ' ' | 企业税号 |
| 14 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_org |  | fid |
