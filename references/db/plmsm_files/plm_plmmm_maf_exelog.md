# 执行物料申请单日志-plm_plmmm_maf_exelog

## 详细错误-子表 t_plmmm_exelog_detail

- **表名称：** 详细错误-子表
- **表名：** t_plmmm_exelog_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frow | 行数 | int4 | 32 |  | √ | 0 | 行数 |
| 3 | ferrormsg | 失败原因 | varchar | 512 |  | √ | ' ' | 失败原因 |
| 4 | fmodelid | 模型名称 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 8 | fmaterialname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmmm_exelog_detail |  | fentryid |
| 2 | idx_plmmm_exelog_detail |  | fid |

---

## 执行物料申请单日志-多语言表 t_plmmm_exelog_l

- **表名称：** 执行物料申请单日志-多语言表
- **表名：** t_plmmm_exelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresultmsg | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmmm_exelog_l |  | fid |
| 2 | pk_t_plmmm_exelog_l |  | fpkid |

---

## 执行物料申请单日志-主表 t_plmmm_exelog

- **表名称：** 执行物料申请单日志-主表
- **表名：** t_plmmm_exelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresultmsg | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果 |
| 3 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fmaterialapplyid | 物料申请单id | int8 | 64 |  | √ | 0 | 物料申请单id |
| 6 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmmm_exelog |  | fmaterialapplyid |
| 2 | pk_plmmm_exelog |  | fid |

---

## 详细错误-多语言表 t_plmmm_exelog_detail_l

- **表名称：** 详细错误-多语言表
- **表名：** t_plmmm_exelog_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterialname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmmm_exelog_detail_l |  | fpkid |
| 2 | idx_plmmm_exelog_detail_l |  | fentryid |
