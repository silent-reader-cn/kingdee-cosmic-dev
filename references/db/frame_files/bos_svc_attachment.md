# 附件管理中心-bos_svc_attachment

## 附件管理中心-主表 t_svc_attachment

- **表名称：** 附件管理中心-主表
- **表名：** t_svc_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 附件名称 | varchar | 255 |  | √ | ' ' | 附件名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdisktype | 存贮类型 | bpchar | 1 |  | √ | '0' | 存贮类型,枚举: 0 :文件服务器 1 :图片服务器 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsource | 附件来源 | varchar | 10 |  | √ | '0' | 附件来源,枚举: 0 :未知 1 :附件字段 2 :附件面板 3 :图片字段 4 :引入 5 :引出 6 :打印生成文件 7 :打印资源文件 8 :上传按钮 9 :BOTP a :人员头像 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 10 | fstatus | 附件状态 | bpchar | 1 |  | √ | 'A' | 附件状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsize | 附件大小（字节） | int8 | 64 |  | √ | 0 | 附件大小（字节） |
| 14 | fext | 附件扩展名 | varchar | 20 |  | √ | ' ' | 附件扩展名 |
| 15 | fsort | 排序字段 | int4 | 32 |  | √ | 0 | 排序字段 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fpath | 附件路径 | varchar | 500 |  | √ | ' ' | 附件路径 |
| 18 | fnumber | 附件编码 | varchar | 80 |  | √ | ' ' | 附件编码 |
| 19 | fidentify | 附件标识 | varchar | 120 |  | √ | ' ' | 附件标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_attachment |  | fid |
| 2 | idx_svc_attachment_number |  | fnumber |
| 3 | idx_svc_attachment_path |  | fpath |
| 4 | idx_svc_attachment_source |  | fsource |
| 5 | idx_svc_attachment_identify |  | fidentify |
