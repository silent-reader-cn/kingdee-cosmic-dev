# 知识语料-knl_corpus

## 知识语料-主表 t_knl_corpus

- **表名称：** 知识语料-主表
- **表名：** t_knl_corpus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 知识目录 | int8 | 64 |  | √ | 0 | [知识分组 knl_group](../devgptas_files/knl_group.md) |
| 3 | fcodedes | 代码描述 | varchar | 255 |  | √ | ' ' | 代码描述 |
| 4 | fnotes | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 5 | ffailmsg | 上传信息 | varchar | 255 |  | √ | ' ' | 上传信息 |
| 6 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 7 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 10 | ffilename | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 11 | fmetadatadesc | 元数据描述 | int8 | 64 |  | √ | 0 | [元数据描述 bos_metadata_desc](../devgptas_files/bos_metadata_desc.md) |
| 12 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 13 | fname | 知识名称 | varchar | 50 |  | √ | ' ' | 知识名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | ftstype | 脚本类型 | varchar | 50 |  | √ | ' ' | 脚本类型,枚举: npsEzBqI :操作 rnry3Wse :表单 ZMJMZ50L :列表 H0j7Vznm :移动表单_实体 RIe5s2q5 :移动列表 p1MEoP47 :动态表单 J1oZDEE4 :移动表单 |
| 17 | finputcontent | 用户输入内容 | varchar | 255 |  | √ | ' ' | 用户输入内容 |
| 18 | fhits | 命中次数 | int8 | 64 |  |  | null | 命中次数 |
| 19 | freadvolume | 阅读量 | int8 | 64 |  |  | null | 阅读量 |
| 20 | fknltype | 知识类型 | int8 | 64 |  | √ | 0 | [知识类型 knl_type](../devgptas_files/knl_type.md) |
| 21 | ffailmsg_tag | 上传信息_详情 | text | 0 |  |  | null | 上传信息_详情 |
| 22 | fuploadstatus | 知识库状态 | varchar | 50 |  | √ | ' ' | 知识库状态,枚举: I :未上传 S :上传成功 F :上传失败 |
| 23 | finputcontent_tag | 用户输入内容_详情 | text | 0 |  |  | null | 用户输入内容_详情 |
| 24 | fupdatetime | 社区知识更新时间 | int8 | 64 |  |  | null | 社区知识更新时间 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fdatasource | 数据来源 | int8 | 64 |  | √ | 0 | [数据来源 knl_datasource](../devgptas_files/knl_datasource.md) |
| 27 | fnumber | 知识编码 | varchar | 30 |  | √ | ' ' | 知识编码 |
| 28 | ffilepath | 文件路径 | varchar | 300 |  | √ | ' ' | 文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_knl_corpus |  | fnumber |
| 2 | pk_t_knl_corpus |  | fid |

---

## 分块信息-子表 t_article_segment

- **表名称：** 分块信息-子表
- **表名：** t_article_segment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsegment | 分段字段 | varchar | 255 |  | √ | ' ' | 分段字段 |
| 3 | fsegtime | 分段时间 | int8 | 64 |  |  | null | 分段时间 |
| 4 | fseghits | 命中次数 | int8 | 64 |  |  | null | 命中次数 |
| 5 | fsegment_tag | 分段字段_详情 | text | 0 |  |  | null | 分段字段_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fassociation | 分段关联 | varchar | 1000 |  | √ | ' ' | 分段关联 |
| 8 | fsegenable | 启用禁用 | varchar | 50 |  | √ | '0' | 启用禁用 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_article_segment_seq |  | fseq |
| 2 | pk_t_article_segment |  | fentryid |

---

## 知识语料-多语言表 t_knl_corpus_l

- **表名称：** 知识语料-多语言表
- **表名：** t_knl_corpus_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 知识名称 | varchar | 50 |  | √ | ' ' | 知识名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_knl_corpus_l |  | fpkid |
| 2 | idx_knl_corpus_l_0 |  | fid,flocaleid |
