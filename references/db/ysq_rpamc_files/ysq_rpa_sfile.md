# 文件管理-ysq_rpa_sfile

## 文件管理-主表 tk_ysq_rpa_sfile

- **表名称：** 文件管理-主表
- **表名：** tk_ysq_rpa_sfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_source_user_id | 文件来源用户ID | int8 | 64 |  |  | null | 文件来源用户ID |
| 3 | fk_ysq_last_oper_type | 最后操作类型 | varchar | 50 |  | √ | ' ' | 最后操作类型,枚举: webCreate :服务器新建 webCover :服务器覆盖 webModDesc :服务器修改描述 webCopy :服务器复制 robCreate :客户端新建 robCover :客户端覆盖 robModDesc :客户端修改描述 thirdCreate :第三方新建 thirdCover :第三方覆盖 thirdModDesc :第三方修改描述 forward :转发 |
| 4 | fk_ysq_create_user_name | 创建人 | varchar | 128 |  | √ | ' ' | 创建人 |
| 5 | fk_ysq_org_id | 创建人部门id | int8 | 64 |  |  | null | 创建人部门id |
| 6 | fk_ysq_opt_desc | 文件操作描述 | varchar | 254 |  | √ | ' ' | 文件操作描述 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_ysq_file_desc | 文件描述 | varchar | 254 |  | √ | ' ' | 文件描述 |
| 9 | fk_ysq_file_tag | 文件标签 | varchar | 512 |  | √ | ' ' | 文件标签 |
| 10 | fk_ysq_agent_no | 机器人编号 | varchar | 128 |  | √ | ' ' | 机器人编号 |
| 11 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 12 | fk_ysq_is_third | 是否第三方 | bpchar | 1 |  | √ | '0' | 是否第三方 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fk_ysq_last_oper_time | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 15 | fk_ysq_file_name_low | 文件名称小写 | varchar | 254 |  | √ | ' ' | 文件名称小写 |
| 16 | fk_ysq_sour_proc_code | 文件来源流程 | varchar | 64 |  | √ | ' ' | 文件来源流程 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fk_ysq_file_name | 文件文件夹名 | varchar | 254 |  | √ | ' ' | 文件文件夹名 |
| 19 | fk_ysq_user_name | 用户名 | varchar | 128 |  |  | NULL | 用户名 |
| 20 | fk_ysq_file_size | 文件大小，字节 | int8 | 64 |  |  | null | 文件大小，字节 |
| 21 | fk_ysq_agent_type | 终端类型 | varchar | 50 |  | √ | ' ' | 终端类型,枚举: robot :机器人 standardRobot :通用机器人 studio :设计器 |
| 22 | fk_ysq_file_count | 文件数量统计 | int8 | 64 |  |  | null | 文件数量统计 |
| 23 | fk_ysq_cur_org_name | 创建人部门名称 | varchar | 64 |  | √ | ' ' | 创建人部门名称 |
| 24 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 25 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fk_ysq_file_type | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: doc :Word docx :Word xls :Excel xlsx :Excel csv :Excel ppt :PPT pptx :PPT txt :文本文件 pdf :Pdf png :图片 jpg :图片 jpeg :图片 bmp :图片 rar :压缩文件 zip :压缩文件 |
| 30 | fk_ysq_operator | 操作人 | int8 | 64 |  |  | null | 操作人 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fk_ysq_sch_name | 调度名称 | varchar | 64 |  | √ | ' ' | 调度名称 |
| 33 | fk_ysq_job_no | 任务编号 | varchar | 64 |  | √ | ' ' | 任务编号 |
| 34 | fk_ysq_agent_alias | 机器人别名 | varchar | 128 |  | √ | ' ' | 机器人别名 |
| 35 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fk_ysq_file_create_type | 文件创建类型 | varchar | 50 |  | √ | ' ' | 文件创建类型,枚举: 0 :页面上传 1 :设计器上传 2 :机器人上传 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_sfile |  | fid |
