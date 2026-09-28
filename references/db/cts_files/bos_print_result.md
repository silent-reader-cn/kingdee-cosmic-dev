# 打印结果-bos_print_result

## 打印结果-主表 t_svc_printresult

- **表名称：** 打印结果-主表
- **表名：** t_svc_printresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | formid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 3 | fprinter | 打印机名称 | varchar | 256 |  | √ | ' ' | 打印机名称 |
| 4 | fdisktype | 文件存贮类型 | bpchar | 1 |  | √ | '1' | 文件存贮类型,枚举: 0 :附件服务器(未知） T :附件服务器（临时） P :附件服务器（永久） 2 :临时服务器 |
| 5 | fexptype | 打印类型 | varchar | 20 |  | √ | ' ' | 打印类型,枚举: pdf :Pdf xls :Excel client :客户端 png :图片 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fservicen | 服务编码 | varchar | 50 |  | √ | ' ' | 服务编码 |
| 9 | ftaskname | 任务名称 | varchar | 256 |  | √ | ' ' | 任务名称 |
| 10 | fappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 11 | fstatus | 打印状态 | bpchar | 1 |  | √ | 'A' | 打印状态,枚举: A :打印中 B :打印完成 C :打印失败 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fext | 扩展参数 | varchar | 256 |  | √ | ' ' | 扩展参数 |
| 14 | ftaskid | 任务编号 | varchar | 50 |  | √ | ' ' | 任务编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idex_svc_printresult_taskid |  | ftaskid |
| 2 | idx_svc_printresult_servicen |  | fservicen |
| 3 | pk_t_svc_printresult |  | fid |

---

## 单据体-子表 t_svc_printresult_detail

- **表名称：** 单据体-子表
- **表名：** t_svc_printresult_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | filetype | 文件类型 | varchar | 20 |  | √ | ' ' | 文件类型 |
| 3 | filename | 文件名称 | varchar | 150 |  | √ | ' ' | 文件名称 |
| 4 | filepath | 文件地址 | varchar | 500 |  | √ | ' ' | 文件地址 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsource | 来源 | bpchar | 1 |  | √ | 'B' | 来源,枚举: A :旧打印 B :新打印 C :新打印（富文本） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_svc_printresult_detail_fid |  | fid |
| 2 | pk_t_svc_printresult_detail |  | fentryid |
