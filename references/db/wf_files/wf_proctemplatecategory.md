# 流程模板分类-wf_proctemplatecategory

## 流程模板分类-多语言表 t_wf_proctplcategory_l

- **表名称：** 流程模板分类-多语言表
- **表名：** t_wf_proctplcategory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_proctplcategory_l |  | fid,flocaleid |
| 2 | pk_wf_proctplcategory_l |  | fpkid |

---

## 流程模板分类-主表 t_wf_proctplcategory

- **表名称：** 流程模板分类-主表
- **表名：** t_wf_proctplcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fapplicationid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 7 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 流程模板分类 wf_proctemplatecategory |
| 8 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fprocesstype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 NoCodeFlow :无代码流程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_proctplcategory_parent |  | fparentid |
| 2 | idx_wf_proctplcategory_appid |  | fapplicationid |
| 3 | idx_wf_proctplcategory_number |  | fnumber |
| 4 | pk_wf_proctplcategory |  | fid |
