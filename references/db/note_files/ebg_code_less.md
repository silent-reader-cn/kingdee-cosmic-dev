# 银行接口配置管理-ebg_code_less

## 文件上传内容单据体-子表 t_note_codeless_filecont

- **表名称：** 文件上传内容单据体-子表
- **表名：** t_note_codeless_filecont

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 文件内容取值来源 | varchar | 50 |  | √ | ' ' | 文件内容取值来源,枚举: ebg_field :银企属性 judging_condition :匹配规则集合 default :固定值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 5 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 6 | fbodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 7 | fexample | 固定值 | varchar | 100 |  | √ | ' ' | 固定值 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fjudging_condition | fjudging_condition | varchar | 50 |  | √ | ' ' |  |
| 10 | fjudging_conditions | 匹配规则集合 | int8 | 64 |  | √ | 0 | [匹配规则集合 ebg_judging_conditions](../note_files/ebg_judging_conditions.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |
| 13 | fmust | 为空时是否上送银行字段 | varchar | 50 |  | √ | ' ' | 为空时是否上送银行字段,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_codeless_filecont_fk |  | fid |
| 2 | pk_note_codeless_filecont |  | fentryid |

---

## 银行接口配置管理-多语言表 t_aqap_code_less_l

- **表名称：** 银行接口配置管理-多语言表
- **表名：** t_aqap_code_less_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_code_less_l |  | fpkid |
| 2 | idx_aqap_code_less_l_0 |  | fid,flocaleid |

---

## 文件名组成单据体-子表 t_note_codeless_filename

- **表名称：** 文件名组成单据体-子表
- **表名：** t_note_codeless_filename

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 文件名取值来源 | varchar | 50 |  | √ | ' ' | 文件名取值来源,枚举: ebg_field :银企属性 judging_condition :匹配规则集合 default :固定值 |
| 3 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 4 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 5 | fbodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fexample | 固定值 | varchar | 100 |  | √ | ' ' | 固定值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fjudging_condition | fjudging_condition | varchar | 50 |  | √ | ' ' |  |
| 10 | fjudging_conditions | 匹配规则集合 | int8 | 64 |  | √ | 0 | [匹配规则集合 ebg_judging_conditions](../note_files/ebg_judging_conditions.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_codeless_filename_fk |  | fid |
| 2 | pk_note_codeless_filename |  | fentryid |

---

## 外层响应码单据体-子表 t_note_out_rspcode

- **表名称：** 外层响应码单据体-子表
- **表名：** t_note_out_rspcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frsp_result | 交易状态 | varchar | 50 |  | √ | ' ' | 交易状态,枚举: ERROR :外层抛出异常 SUBMITED :银行处理中 FAIL :交易失败 UNKNOWN :交易未确认 MIDDLE :中间状态，等待内层状态码校验结果 |
| 3 | frsp_judging | frsp_judging | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frsp_out_judgings | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则 ebg_judging_condition](../note_files/ebg_judging_condition.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_out_rspcode_fk |  | fid |
| 2 | pk_note_out_rspcode |  | fentryid |

---

## 银行接口配置管理-主表 t_aqap_code_less

- **表名称：** 银行接口配置管理-主表
- **表名：** t_aqap_code_less

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 银行版本.应用 | int8 | 64 |  | √ | 0 | [银行应用列表 note_bank_app_list](../note_files/note_bank_app_list.md) |
| 3 | fcur_setter | 下拉列表23 | varchar | 10 |  |  | '0' | 下拉列表23,枚举: |
| 4 | ffilename_split | 文件名分隔符 | varchar | 50 |  | √ | ' ' | 文件名分隔符 |
| 5 | fbiz_type_number | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: notePayable :应付票据 noteReceivable :应收票据 queryNoteDetail :待签收票据查询 queryNoteInfo :贴现试算查询 queryNoteSide :背面信息查询 |
| 6 | fdebit_type | 文本38 | varchar | 10 |  |  | ' ' | 文本38 |
| 7 | fbiz_type | fbiz_type | int8 | 64 |  | √ | 0 |  |
| 8 | ftrans_code | 银行接口代码 | varchar | 50 |  | √ | ' ' | 银行接口代码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ffile_split | 文件内容分隔符 | varchar | 50 |  | √ | ' ' | 文件内容分隔符 |
| 11 | ffirst_tag | 首页页码/起始位置 | varchar | 50 |  |  | ' ' | 首页页码/起始位置 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffile_head | 文件内容头 | varchar | 500 |  | √ | 0 | 文件内容头 |
| 16 | fcd_setter | 下拉列表23 | varchar | 10 |  |  | ' ' | 下拉列表23,枚举: |
| 17 | fis_need_page | 是否设置分页 | bpchar | 1 |  |  | '0' | 是否设置分页 |
| 18 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ffile_biztype | 代理程序bizType | varchar | 50 |  | √ | ' ' | 代理程序bizType |
| 21 | ffilename_suffix | 文件名后缀 | varchar | 50 |  | √ | ' ' | 文件名后缀,枚举: .txt :.txt .xls :.xls none :无后缀 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fcontenttype | 格式 | varchar | 50 |  | √ | ' ' | 格式,枚举: xml :xml json :json cdata_xml :xml（带CDATA标签） |
| 24 | fnote_interface | fnote_interface | int8 | 64 |  | √ | 0 |  |
| 25 | fcredit_type | 文本38 | varchar | 10 |  |  | ' ' | 文本38 |
| 26 | fbiz_type_new | 业务类型 | int8 | 64 |  |  | null | [低代码业务类型 note_codeless_type](../note_files/note_codeless_type.md) |
| 27 | ffile_head_tag | 文件内容头_详情 | text | 0 |  |  | null | 文件内容头_详情 |
| 28 | fis_fileupload | 是否文件上传 | bpchar | 1 |  | √ | '0' | 是否文件上传 |
| 29 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_code_less |  | fid |
| 2 | idx_aqap_code_less |  | fbiz_type_number,ftrans_code |

---

## 内层响应码单据体-子表 t_note_inner_rspcode

- **表名称：** 内层响应码单据体-子表
- **表名：** t_note_inner_rspcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frsp_result | 交易状态 | varchar | 50 |  | √ | ' ' | 交易状态,枚举: SUBMITED :银行处理中 SUCCESS :交易成功 FAIL :交易失败 UNKNOWN :交易未确认 REFUSE :被对手方拒签 |
| 3 | frsp_judging | frsp_judging | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frsp_inner_judging | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则 ebg_judging_condition](../note_files/ebg_judging_condition.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_inner_rspcode |  | fentryid |
| 2 | idx_note_inner_rspcode_fk |  | fid |

---

## 响应体单据体-子表 t_note_codeless_rspbody

- **表名称：** 响应体单据体-子表
- **表名：** t_note_codeless_rspbody

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpage_param_type | 分页参数字段设置 | varchar | 50 |  |  | ' ' | 分页参数字段设置,枚举: Bank_Total_PAGE :银行总页数 Bank_Total_REC :银行总记录数 Bake_Next_PAGE :银行下一页页码 Bank_PageREQ_REC :银行每页查询记录数 Bank_PageRET_REC :银行每页返回记录数 last_Page :银行最后一页标记 |
| 3 | frsp_match | 银企匹配字段 | varchar | 150 |  | √ | ' ' | 银企匹配字段,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparse_judging_conditions | 匹配规则集合 | int8 | 64 |  |  | 0 | [匹配规则集合 ebg_judging_conditions](../note_files/ebg_judging_conditions.md) |
| 6 | frsp_paramnode | 报文节点 | varchar | 150 |  | √ | ' ' | 报文节点,枚举: structure_node :结构节点 business_node :业务节点 repeat_node :循环节点 attribute_node :属性节点 |
| 7 | frsp_paramname | 银行字段 | varchar | 150 |  | √ | ' ' | 银行字段 |
| 8 | frsp_code_field | 响应字段类型 | varchar | 150 |  | √ | ' ' | 响应字段类型,枚举: other :非状态码字段 out_code :外层状态码字段 inner_code :内层状态码字段 inner_code2 :内层状态码字段2 inner_code3 :内层状态码字段3 out_msg :外层状态码描述字段 inner_msg :内层状态码描述字段 json_map :解析域字段 cd_flag :借贷标识字段 amount :交易金额字段 kd_flag :对账码字段 |
| 9 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 10 | frsp_bodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | frsp_paramdes | 银行字段名称 | varchar | 150 |  | √ | ' ' | 银行字段名称 |
| 13 | frsp_ebgparam | 填入银企字段 | varchar | 150 |  | √ | ' ' | 填入银企字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_codeless_rspbody_fk |  | fid |
| 2 | idx_note_codeless_rspbody |  | frsp_paramname |
| 3 | pk_note_codeless_rspbody |  | fentryid |

---

## 请求体单据体-子表 t_note_codeless_bodyentry

- **表名称：** 请求体单据体-子表
- **表名：** t_note_codeless_bodyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 银行字段取值来源 | varchar | 50 |  | √ | ' ' | 银行字段取值来源,枚举: ebg_field :银企属性 judging_condition :匹配规则集合 default :固定值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparamtype | （隐藏）字段类型 | varchar | 50 |  | √ | ' ' | （隐藏）字段类型,枚举: String :String Long :Long int :int Boolean :Boolean Double :Double Float :Float Object :Object Array :Array |
| 5 | fparamnode | 报文节点 | varchar | 50 |  | √ | ' ' | 报文节点,枚举: structure_node :结构节点 business_node :业务节点 repeat_node :循环节点 |
| 6 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 7 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 8 | fparamname | 银行字段 | varchar | 50 |  | √ | ' ' | 银行字段 |
| 9 | fbodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 10 | fexample | 固定值 | varchar | 100 |  | √ | ' ' | 固定值 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fparamdesc | 银行字段名称 | varchar | 50 |  | √ | ' ' | 银行字段名称 |
| 13 | fjudging_condition | fjudging_condition | varchar | 50 |  | √ | ' ' |  |
| 14 | fjudging_conditions | 匹配规则集合 | int8 | 64 |  | √ | 0 | [匹配规则集合 ebg_judging_conditions](../note_files/ebg_judging_conditions.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |
| 17 | fmust | 为空时是否上送银行字段 | varchar | 50 |  | √ | ' ' | 为空时是否上送银行字段,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_codeless_bodyentry |  | fentryid |
| 2 | idx_note_codeless_bodyentry_fk |  | fid |
| 3 | idx_note_codeless_bodyentry |  | fparamname |

---

## 最后一页单据体-子表 t_lastpage_entity

- **表名称：** 最后一页单据体-子表
- **表名：** t_lastpage_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fresult | 匹配结果 | varchar | 50 |  | √ | ' ' | 匹配结果,枚举: 1 :是最后一页 0 :非最后一页 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | flastpage_scheme | 预置方案 | int8 | 64 |  |  | null | [分页方案 ebg_page_scheme](../note_files/ebg_page_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_lastpage_entity_pkey |  | fentryid |

---

## 下一页设置单据体-子表 t_nextpage_entity

- **表名称：** 下一页设置单据体-子表
- **表名：** t_nextpage_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 4 | fnextpage_scheme | 方案 | int8 | 64 |  |  | null | [分页方案 ebg_page_scheme](../note_files/ebg_page_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_nextpage_entity_pkey |  | fentryid |

---

## 文件上传请求体单据体-子表 t_note_codeless_fileentry

- **表名称：** 文件上传请求体单据体-子表
- **表名：** t_note_codeless_fileentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 银行字段取值来源 | varchar | 50 |  | √ | ' ' | 银行字段取值来源,枚举: ebg_field :银企属性 judging_condition :判断条件 default :固定值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparamtype | （隐藏）字段类型 | varchar | 50 |  | √ | ' ' | （隐藏）字段类型,枚举: String :String Long :Long int :int Boolean :Boolean Double :Double Float :Float Object :Object Array :Array |
| 5 | fparamnode | 报文节点 | varchar | 50 |  | √ | ' ' | 报文节点,枚举: structure_node :结构节点 business_node :业务节点 repeat_node :循环节点 |
| 6 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 7 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 8 | fparamname | 银行字段 | varchar | 50 |  | √ | ' ' | 银行字段 |
| 9 | fbodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 10 | fexample | 固定值 | varchar | 100 |  | √ | ' ' | 固定值 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fjudging_condition | 判断条件 | varchar | 50 |  | √ | ' ' | 判断条件 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fparamdes | 银行字段名称 | varchar | 50 |  | √ | ' ' | 银行字段名称 |
| 15 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |
| 16 | fmust | 为空时是否上送银行字段 | varchar | 50 |  | √ | ' ' | 为空时是否上送银行字段,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_codeless_fileentry |  | fentryid |
| 2 | idx_note_codeless_fileentry |  | fparamname |
| 3 | idx_note_codeless_fileentry_fk |  | fid |

---

## 请求头单据体-子表 t_note_codeless_headerent

- **表名称：** 请求头单据体-子表
- **表名：** t_note_codeless_headerent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheaderdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fheadervalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 4 | fheadername | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_codeless_headerent_fk |  | fid |
| 2 | pk_note_codeless_headerent |  | fentryid |
| 3 | idx_note_codeless_headerent |  | fheadername |
