# 集成方案-星空(停用)-eafc_xk_project

## 内容单据体-子表 tk_eafc_project_content

- **表名称：** 内容单据体-子表
- **表名：** tk_eafc_project_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_content | 内容 | int8 | 64 |  |  | null | [集成内容-星空(停用) eafc_xk_content](../ecollect_files/eafc_xk_content.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_project_content |  | fentryid |
| 2 | idx__eafc_project_content_fk |  | fid |

---

## 集成方案-星空(停用)-主表 tk_eafc_xk_project

- **表名称：** 集成方案-星空(停用)-主表
- **表名：** tk_eafc_xk_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fk_eafc_period_end | 归档期间.结束 | timestamp | 0 |  |  | null | 归档期间.结束 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_eafc_period_start | 归档期间.开始 | timestamp | 0 |  |  | null | 归档期间.开始 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fk_eafc_textfield | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 11 | fk_eafc_system | 集成系统 | int8 | 64 |  |  | null | [集成系统-星空(停用) eafc_xk_system](../ecollect_files/eafc_xk_system.md) |
| 12 | fk_eafc_desc | 方案描述 | varchar | 50 |  | √ | ' ' | 方案描述 |
| 13 | fbillno | 方案编号 | varchar | 30 |  | √ | ' ' | 方案编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_xk_project |  | fid |

---

## 组织单据体-子表 tk_eafc_project_org

- **表名称：** 组织单据体-子表
- **表名：** tk_eafc_project_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_project_org |  | fentryid |
| 2 | idx__eafc_project_org_fk |  | fid |
