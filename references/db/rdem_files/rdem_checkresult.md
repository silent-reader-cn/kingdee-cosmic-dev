# 检查报告-rdem_checkresult

## 单据体-子表 t_pca_checkresultentry

- **表名称：** 单据体-子表
- **表名：** t_pca_checkresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcnsmtime | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | flinkinfo | 联查信息 | varchar | 2000 |  | √ | ' ' | 联查信息 |
| 5 | fitem | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 6 | fotherinfo | 其他信息 | varchar | 2000 |  | √ | ' ' | 其他信息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fitemresult | 检查结果 | varchar | 50 |  | √ | ' ' | 检查结果,枚举: A :通过 B :错误 C :警告 D :异常 E :运行中 F :跳过· |
| 9 | fotherinfo_tag | 其他信息_详情 | text | 0 |  |  | null | 其他信息_详情 |
| 10 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_checkresultentry |  | fentryid |
| 2 | idx_pca_checkresultentry_fid |  | fid |

---

## 检查报告-主表 t_pca_checkresult

- **表名称：** 检查报告-主表
- **表名：** t_pca_checkresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fresult | 检查结果 | varchar | 50 |  | √ | ' ' | 检查结果,枚举: A :通过 B :错误 C :警告 D :异常 E :运行中 F :跳过 |
| 9 | fuserid | 执行用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftype | 检查类型 | varchar | 50 |  | √ | ' ' | 检查类型,枚举: A :成本计算 B :结账 |
| 14 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 15 | ftaskid | 检查任务号 | varchar | 255 |  | √ | ' ' | 检查任务号 |
| 16 | ftotalcnsmtime | 总耗时（秒） | int8 | 64 |  | √ | 0 | 总耗时（秒） |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_checkresult_taskid |  | ftaskid |
| 2 | pk_pca_checkresult |  | fid |
| 3 | idx_pca_checkresult_bno |  | fbillno |

---

## 单据体-多语言表 t_pca_checkresultentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_pca_checkresultentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fitem | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_checkresultentry_l_id |  | fentryid,flocaleid |
| 2 | pk_pca_checkresultentry_l |  | fpkid |

---

## 子单据体-子表 t_pca_checkresultsubentry

- **表名称：** 子单据体-子表
- **表名：** t_pca_checkresultsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailinfo | 详情 | varchar | 2000 |  | √ | ' ' | 详情 |
| 2 | fobjid | 异常对象id | int8 | 64 |  | √ | 0 | 异常对象id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fobjtype | 异常对象类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fobjdes | 异常对象描述 | varchar | 2000 |  | √ | ' ' | 异常对象描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_checkresultsubentry_fentryid |  | fentryid |
| 2 | pk_pca_checkresultsubentry |  | fdetailid |
