# 文档分类历史-cvp_cls_history

## 单据体-子表 t_cvp_cls_filetask

- **表名称：** 单据体-子表
- **表名：** t_cvp_cls_filetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilecontent_tag | 提取结果_详情 | text | 0 |  |  | null | 提取结果_详情 |
| 3 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 4 | ffilecontent | 提取结果 | varchar | 255 |  |  | null | 提取结果 |
| 5 | fextractid | 提取任务id | int8 | 64 |  | √ | 0 | 提取任务id |
| 6 | ftemplateftype | 模板字段类型 | varchar | 50 |  |  | null | 模板字段类型,枚举: 1 :普通模板字段 2 :大模型字段 3 :混合模板字段 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fprogress | 进度或错误提示词 | varchar | 255 |  |  | ' ' | 进度或错误提示词 |
| 9 | fisrec | 是否识别 | bpchar | 1 |  | √ | '0' | 是否识别 |
| 10 | fstatus | 子任务状态 | varchar | 50 |  | √ | 'running' | 子任务状态,枚举: running :运行中 extractSuc :提取文本完成 classifySuc :分类完成 recSuc :识别完成 success :任务完成 error :任务失败 |
| 11 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fllmclsid | 大模型分类任务id | int8 | 64 |  | √ | 0 | 大模型分类任务id |
| 13 | fclsfileid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 14 | ffilename | 文件名称 | varchar | 255 |  |  | null | 文件名称 |
| 15 | ftempformid | 模板formid | varchar | 50 |  |  | null | 模板formid |
| 16 | fpagesize | 总页码数 | int4 | 32 |  | √ | 0 | 总页码数 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fdoctypename | 文件类别 | varchar | 50 |  |  | null | 文件类别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cvp_cls_filetask |  | fclsfileid,fextractid,fllmclsid |
| 2 | pk_t_cvp_cls_filetask |  | fentryid |

---

## 子单据体-子表 t_cvp_cls_result

- **表名称：** 子单据体-子表
- **表名：** t_cvp_cls_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frectaskid | 识别提取任务id | int8 | 64 |  | √ | 0 | 识别提取任务id |
| 2 | fpagenum | 页码数 | int4 | 32 |  | √ | 0 | 页码数 |
| 3 | ftargetfileid | 图片id | int8 | 64 |  | √ | 0 | 图片id |
| 4 | ftargetstatus | 图片任务状态 | varchar | 50 |  |  | null | 图片任务状态 |
| 5 | ftargetprogres | 图片任务进度或异常提示词 | varchar | 255 |  |  | ' ' | 图片任务进度或异常提示词 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | ftargeturl | 图片路径 | varchar | 1000 |  |  | null | 图片路径 |
| 10 | frecresult | 识别结果 | varchar | 255 |  |  | null | 识别结果 |
| 11 | frecresult_tag | 识别结果_详情 | text | 0 |  |  | null | 识别结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cvp_cls_result |  | frectaskid |
| 2 | pk_t_cvp_cls_result |  | fdetailid |

---

## 文档分类历史-主表 t_cvp_cls_history

- **表名称：** 文档分类历史-主表
- **表名：** t_cvp_cls_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclsinfo | 组合识别器 | int8 | 64 |  | √ | 0 | [文档分类 cvp_cls_info](../cvp_files/cvp_cls_info.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fllmclstype | 大模型分类方式 | varchar | 10 |  | √ | '1' | 大模型分类方式,枚举: 1 :普通大模型分类 2 :多模态大模型分类 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fextracttype | 提取文字方式 | varchar | 10 |  |  | ' ' | 提取文字方式,枚举: 1 :通用文字 2 :复杂文档提取（文档提取V1、V2） 3 :复杂文档提取（图片切分） |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsource | 请求来源 | varchar | 10 |  |  | 'D' | 请求来源,枚举: A :低代码按钮 B :微服务 C :openapi D :界面测试 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fllmnumber | 分类大模型编码 | varchar | 80 |  | √ | ' ' | 分类大模型编码 |
| 12 | fistest | 是否测试任务 | bpchar | 1 |  | √ | '1' | 是否测试任务 |
| 13 | fbizbillid | 业务单据id | varchar | 50 |  |  | null | 业务单据id |
| 14 | ftext_extract_model | 文档解析模型 | varchar | 80 |  | √ | ' ' | 文档解析模型 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fclatype | 分类方法 | varchar | 10 |  | √ | '3' | 分类方法,枚举: 1 :关键字 2 :图片 3 :大模型 |
| 17 | fbizobj | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  |  | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_cls_history |  | fid |
| 2 | inx_t_cvp_cls_history |  | fbillno,fbillstatus |
