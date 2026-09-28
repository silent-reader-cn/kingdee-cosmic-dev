# 外部数据模型分录-fah_ext_dataentry

## 外部数据模型分录-主表 t_fah_ext_modflds

- **表名称：** 外部数据模型分录-主表
- **表名：** t_fah_ext_modflds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 数据字段分组定义 fah_ext_model_fldgrp |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | frequiredcondition | 必录条件 | text | 0 |  |  | null | 必录条件 |
| 5 | fmodelid | 数据模型 | int8 | 64 |  | √ | 0 | 异构数据对接模型 fah_ext_datamodel |
| 6 | fseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 7 | fassistprop | 辅助资料 | int8 | 64 |  | √ | 0 | 辅助资料分类 bos_assistantdatagroup |
| 8 | fbaseprop | 基础资料 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 9 | frequired | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |
| 10 | fvisable | 显示 | bpchar | 1 |  | √ | ' ' | 显示 |
| 11 | fproperties_tag | 字段属性 | text | 0 |  |  | null | 字段属性 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fdatatype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 0 :日期 1 :基础资料 2 :基础 3 :浮点数 4 :整数 5 :布尔型 6 :字符串 7 :金额：精度限制2位 98 :分录 99 :上传的文件附件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fah_ext_modflds_mg |  | fmodelid,fgroupid |
| 2 | pk_fah_ext_modflds |  | fid |
