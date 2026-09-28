# 推送内容-ipop_recommend

## 推送内容-主表 t_ipop_recommend

- **表名称：** 推送内容-主表
- **表名：** t_ipop_recommend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdirecturl | 详情链接 | varchar | 2000 |  | √ | ' ' | 详情链接 |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fslidepicus | 轮播图-英文 | varchar | 500 |  | √ | ' ' | 轮播图-英文 |
| 6 | fsubtitle | 副标题 | varchar | 255 |  | √ | ' ' | 副标题 |
| 7 | frecommendid | 推荐ID | int8 | 64 |  | √ | 0 | 推荐ID |
| 8 | ficonpic | 特性ICON | varchar | 500 |  | √ | ' ' | 特性ICON |
| 9 | ftitle | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :禁用 |
| 11 | fenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 12 | fslidepiccn | 轮播图-中文 | varchar | 500 |  | √ | ' ' | 轮播图-中文 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstartdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 16 | fslidepic | 轮播图 | varchar | 500 |  | √ | ' ' | 轮播图 |
| 17 | forder | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 18 | fdesc | 详细描述 | varchar | 2000 |  | √ | ' ' | 详细描述 |
| 19 | fvideourl | 视频链接 | varchar | 2000 |  | √ | ' ' | 视频链接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_recommend_cr_d |  | fcreatedate |
| 2 | pk_t_ipop_recommend |  | fid |
