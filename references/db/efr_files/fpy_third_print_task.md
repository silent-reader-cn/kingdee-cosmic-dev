# 第三方打印任务-fpy_third_print_task

## 单据体-子表 tk_fpy_third_print_task_i

- **表名称：** 单据体-子表
- **表名：** tk_fpy_third_print_task_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fk_fpy_filename | 文件名 | varchar | 100 |  | √ | ' ' | 文件名 |
| 4 | fk_fpy_filesign | 文件提名 | varchar | 500 |  | √ | ' ' | 文件提名 |
| 5 | fk_fpy_filedesc | 文件描述 | varchar | 500 |  | √ | ' ' | 文件描述 |
| 6 | fk_fpy_fileurl | 文件路径 | varchar | 200 |  | √ | ' ' | 文件路径 |
| 7 | fk_fpy_filestatus | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 0 :待上传 1 :上传成功 2 :上传失败 3 :待打印 4 :正在打印 5 :打印成功 6 :打印失败 7 :已取消 |
| 8 | fk_fpy_filetype | 文本格式 | varchar | 50 |  | √ | ' ' | 文本格式 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__fpy_third_print_task_i_fk |  | fid |
| 2 | pk__fpy_third_print_task_i |  | fentryid |

---

## 第三方打印任务-主表 tk_fpy_third_print_task

- **表名称：** 第三方打印任务-主表
- **表名：** tk_fpy_third_print_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_fpy_process | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_fpy_status | 批次状态 | varchar | 50 |  | √ | ' ' | 批次状态,枚举: 0 :待拉取 1 :待打印 2 :正在打印 3 :打印成功 4 :打印失败 5 :已取消 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_fpy_desc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 12 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_third_print_task |  | fid |
