# 标书文件-pds_biddocentryf7

## 标书文件-主表 t_pds_biddoc_content

- **表名称：** 标书文件-主表
- **表名：** t_pds_biddoc_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ffilename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcontent_tag | 标书内容_详情 | text | 0 |  |  | null | 标书内容_详情 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbiddoctplld | 标书模板 | int8 | 64 |  | √ | 0 | 公告模板配置 pds_noticetpl |
| 9 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 10 | fcontent | 标书内容 | varchar | 255 |  | √ | ' ' | 标书内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_biddoc_content |  | fid |
| 2 | idx_pds_biddoc_content_pid |  | fprojectid |
