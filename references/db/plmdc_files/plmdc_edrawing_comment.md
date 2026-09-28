# Edrawing批注-plmdc_edrawing_comment

## 单据体-子表 t_plmdc_edrawing_reply

- **表名称：** 单据体-子表
- **表名：** t_plmdc_edrawing_reply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freplycontent | 回复内容 | varchar | 500 |  | √ | ' ' | 回复内容 |
| 3 | freplycreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | freplycreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | freplystatus | 状态 | varchar | 1 |  | √ | '0' | 状态,枚举: 0 :未解决 1 :已解决 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_edrwing_reply_fentryid |  | fid |
| 2 | pk_t_plmdc_edrawing_reply |  | fentryid |

---

## Edrawing批注-主表 t_plmdc_edrawing_comment

- **表名称：** Edrawing批注-主表
- **表名：** t_plmdc_edrawing_comment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigincontent | 来源内容 | varchar | 50 |  | √ | ' ' | 来源内容 |
| 3 | fstatus | 批注状态 | varchar | 1 |  | √ | '0' | 批注状态,枚举: 0 :未解决 1 :已解决 |
| 4 | foriginid | 来源ID | varchar | 255 |  | √ | ' ' | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcommentcontent | 批注内容 | varchar | 500 |  | √ | ' ' | 批注内容 |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpositioninfodata | 位置信息 | varchar | 255 |  | √ | ' ' | 位置信息 |
| 9 | ffileid | 文件ID | int8 | 64 |  | √ | 0 | 文件ID |
| 10 | fpositioninfodata_tag | 位置信息_详情 | text | 0 |  |  | ' ' | 位置信息_详情 |
| 11 | fbillnofield | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_edrawing_comment |  | fid |
| 2 | idx_plmdc_comment_fileid |  | ffileid |
