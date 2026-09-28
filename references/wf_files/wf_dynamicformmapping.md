# 动态表单映射-wf_dynamicformmapping

## 动态表单映射-主表 t_wf_dynamicformmapping

- **表名称：** 动态表单映射-主表
- **表名：** t_wf_dynamicformmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 表单名称 | varchar | 500 |  | √ | ' ' | 表单名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodeltype | 表单类型 | varchar | 50 |  | √ | ' ' | 表单类型,枚举: DynamicFormModel :PC端的动态表单 MobileFormModel :移动版的动态表单 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsourceid | sourceid | varchar | 36 |  | √ | ' ' | sourceid |
| 7 | fmodify | 可修改 | bpchar | 1 |  | √ | '0' | 可修改 |
| 8 | fentitynumber | 实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fdynamicformnumber | 表单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fpreinsdata | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fbusinessenable | 业务使用状态 | varchar | 10 |  | √ | ' ' | 业务使用状态,枚举: 0 :禁用 1 :可用 2 :空 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 10 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 表单编码 | varchar | 30 |  | √ | ' ' | 表单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_dynamicformmapping |  | fid |
| 2 | idx_wf_dynamicformmapping |  | fentitynumber,fbusinessenable,fenable |

---

## 动态表单映射-多语言表 t_wf_dynamicformmapping_l

- **表名称：** 动态表单映射-多语言表
- **表名：** t_wf_dynamicformmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 表单名称 | varchar | 500 |  | √ | ' ' | 表单名称 |
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
| 1 | pk_wf_dynamicformmapping_l |  | fpkid |
| 2 | idx_wf_dynamicformmapping_l |  | fid,flocaleid |
